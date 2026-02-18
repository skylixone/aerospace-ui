#!/usr/bin/env python3
"""
Review Server — A local feedback loop tool.
Dependencies: Python 3.x (Standard Library only)
"""

import sys
import json
import argparse
import logging
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

# Global state
TARGET = None
COMMENTS_FILE = Path("comments.json")

CLIENT_SCRIPT = """
<style>
    .review-overlay { position: fixed; bottom: 20px; right: 20px; background: #09090b; border: 1px solid #27272a; padding: 12px; border-radius: 8px; z-index: 2147483647; color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.5); font-family: sans-serif; display: flex; gap: 8px; align-items: center; }
    .review-mode-active * { cursor: crosshair !important; }
    .review-mode-active *:hover { outline: 2px solid #a855f7 !important; outline-offset: -2px; }
    .review-marker { position: absolute; width: 20px; height: 20px; background: #a855f7; border-radius: 50%; border: 2px solid white; transform: translate(-50%, -50%); z-index: 2147483646; pointer-events: none; }
    
    #comment-dialog { position: fixed; display: none; background: #18181b; border: 1px solid #3f3f46; padding: 16px; border-radius: 8px; width: 300px; z-index: 2147483647; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
    #comment-dialog textarea { width: 100%; height: 80px; background: #09090b; border: 1px solid #27272a; color: white; padding: 8px; border-radius: 4px; margin-bottom: 8px; font-family: inherit; resize: vertical; }
    #comment-dialog button { padding: 6px 12px; border-radius: 4px; border: none; font-weight: 500; cursor: pointer; }
    .btn-primary { background: #a855f7; color: white; }
    .btn-secondary { background: transparent; color: #a1a1aa; }
    .btn-secondary:hover { color: white; }
</style>

<div class="review-overlay">
    <span style="font-size: 12px; font-weight: 500; color: #a1a1aa;">Review Mode</span>
    <button id="toggle-review" class="btn-primary" style="padding: 4px 12px; font-size: 12px;">OFF</button>
</div>

<div id="comment-dialog">
    <h4 style="margin: 0 0 8px 0; font-size: 14px; font-weight: 600; color: white;">Add Comment</h4>
    <textarea id="comment-text" placeholder="What should be changed?"></textarea>
    <div style="display: flex; justify-content: flex-end; gap: 8px;">
        <button class="btn-secondary" onclick="closeDialog()">Cancel</button>
        <button class="btn-primary" onclick="submitComment()">Save</button>
    </div>
</div>

<script>
    let isReviewMode = false;
    let selectedElement = null;
    let activeMarker = null;

    const toggleBtn = document.getElementById('toggle-review');
    const dialog = document.getElementById('comment-dialog');
    const textarea = document.getElementById('comment-text');

    toggleBtn.addEventListener('click', () => {
        isReviewMode = !isReviewMode;
        toggleBtn.textContent = isReviewMode ? "ON" : "OFF";
        toggleBtn.style.backgroundColor = isReviewMode ? "#22c55e" : "#a855f7";
        document.body.classList.toggle('review-mode-active', isReviewMode);
    });

    document.addEventListener('click', (e) => {
        if (!isReviewMode) return;
        if (e.target.closest('.review-overlay') || e.target.closest('#comment-dialog')) return;

        e.preventDefault();
        e.stopPropagation();

        selectedElement = e.target;
        
        const x = Math.min(window.innerWidth - 320, e.clientX + 10);
        const y = Math.min(window.innerHeight - 200, e.clientY + 10);
        
        dialog.style.left = x + 'px';
        dialog.style.top = y + 'px';
        dialog.style.display = 'block';
        textarea.focus();

        if (activeMarker) activeMarker.remove();
        activeMarker = document.createElement('div');
        activeMarker.className = 'review-marker';
        activeMarker.style.left = e.pageX + 'px';
        activeMarker.style.top = e.pageY + 'px';
        document.body.appendChild(activeMarker);
    }, true);

    function closeDialog() {
        dialog.style.display = 'none';
        textarea.value = '';
        if (activeMarker) activeMarker.remove();
        activeMarker = null;
    }

    function getSelector(el) {
        if (el.id) return '#' + el.id;
        if (el.className) {
            const classes = Array.from(el.classList).join('.');
            return el.tagName.toLowerCase() + '.' + classes.split(' ').join('.');
        }
        return el.tagName.toLowerCase();
    }

    async function submitComment() {
        const text = textarea.value.trim();
        if (!text) return;

        const selector = getSelector(selectedElement);
        const snippet = selectedElement.outerHTML.substring(0, 100);
        
        try {
            const res = await fetch('/_review/api/comment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    selector: selector,
                    text: text,
                    snippet: snippet,
                    url: window.location.href
                })
            });
            
            if (res.ok) {
                const btn = document.querySelector('#comment-dialog .btn-primary');
                const originalText = btn.textContent;
                btn.textContent = "Saved!";
                btn.style.backgroundColor = "#22c55e";
                setTimeout(() => {
                    closeDialog();
                    btn.textContent = originalText;
                    btn.style.backgroundColor = "#a855f7";
                }, 800);
            }
        } catch (err) {
            alert("Error saving comment");
            console.error(err);
        }
    }
</script>
"""

class ReviewHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/_review/api/comment':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                print(f"📝 New Comment: {data['text']} on {data['selector']}")
                
                comments = []
                if COMMENTS_FILE.exists():
                    try:
                        with open(COMMENTS_FILE, "r") as f:
                            comments = json.load(f)
                    except: pass
                        
                comments.append(data)
                
                with open(COMMENTS_FILE, "w") as f:
                    json.dump(comments, f, indent=2)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok"}).encode('utf-8'))
            except Exception as e:
                print(f"Error saving comment: {e}")
                self.send_response(500)
                self.end_headers()
        else:
            self.send_error(404)

    def do_GET(self):
        # Translate path to local filesystem
        path = self.translate_path(self.path)
        p = Path(path)
        
        # If directory, look for index.html
        if p.is_dir():
            index = p / "index.html"
            if index.exists():
                p = index
                
        # Handle HTML injection
        if p.is_file() and p.suffix == '.html':
            try:
                with open(p, 'rb') as f:
                    content = f.read()
                
                try:
                    html = content.decode('utf-8')
                    if "</body>" in html:
                        html = html.replace("</body>", f"{CLIENT_SCRIPT}</body>")
                    else:
                        html += CLIENT_SCRIPT
                    content = html.encode('utf-8')
                    
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.send_header("Content-Length", str(len(content)))
                    # Standard CORS/Cache headers
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                    self.end_headers()
                    self.wfile.write(content)
                    return
                except UnicodeDecodeError:
                    # If we can't decode, just serve as is using super logic
                    pass
            except Exception as e:
                print(f"Error serving {p}: {e}")
                
        # Fallback to standard serving for non-HTML or errors
        super().do_GET()

def main():
    global TARGET, COMMENTS_FILE
    
    parser = argparse.ArgumentParser(description="Review Server (No Dependencies)")
    parser.add_argument("target", help="File path or directory", nargs='?', default=".")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    args = parser.parse_args()
    
    target_path = Path(args.target).resolve()
    
    if target_path.is_file():
        # If target is a file, serve the directory containing it, but we can't 'force' serving just one file easily
        # So we just serve the parent dir.
        print(f"📂 Serving directory: {target_path.parent}")
        # Change CWD to the file's directory so relative paths work
        import os
        os.chdir(target_path.parent)
        COMMENTS_FILE = Path("comments.json")
    elif target_path.is_dir():
        print(f"📂 Serving directory: {target_path}")
        import os
        os.chdir(target_path)
        COMMENTS_FILE = Path("comments.json")
    else:
        print(f"❌ Invalid path: {target_path}")
        sys.exit(1)

    print(f"✅ Review Engine Running")
    print(f"📝 Comments: {COMMENTS_FILE.resolve()}")
    print(f"👉 URL: http://localhost:{args.port}")
    if target_path.is_file():
        print(f"👉 Open: http://localhost:{args.port}/{target_path.name}")
    
    httpd = HTTPServer(('localhost', args.port), ReviewHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == "__main__":
    main()
