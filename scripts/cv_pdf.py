"""
Builds the downloadable CV PDF from the /cv/ page of the built site.

Usage:  python scripts/cv_pdf.py <built-site-folder> <output.pdf>
Run automatically by .github/workflows/cv-pdf.yml whenever cv.md changes.
"""
import functools
import http.server
import sys
import threading

from playwright.sync_api import sync_playwright

site_dir, out_pdf = sys.argv[1], sys.argv[2]

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=site_dir)
server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f"http://127.0.0.1:{server.server_port}/cv/"

FOOTER = """
<div style="width:100%;font-family:Inter,Helvetica,Arial,sans-serif;font-size:8px;color:#5a6175;
            padding:0 0.8in;display:flex;justify-content:space-between;">
  <span>Suzanna Krivulskaya · Curriculum Vitae</span>
  <span><span class="pageNumber"></span> of <span class="totalPages"></span></span>
</div>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")
    page.wait_for_function("document.documentElement.classList.contains('cv-ready')")
    page.evaluate("document.fonts.ready")
    page.emulate_media(media="print")
    page.pdf(
        path=out_pdf,
        format="Letter",
        print_background=True,
        prefer_css_page_size=True,
        display_header_footer=True,
        header_template="<span></span>",
        footer_template=FOOTER,
    )
    browser.close()

server.shutdown()
print(f"Wrote {out_pdf}")
