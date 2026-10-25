"""Enable page-wide metadata controls using the imported local method assets."""
def setup(app):
    app.add_js_file('need-controls.js')
    app.add_css_file('need-controls.css')
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
