from eve import Eve
import qrcode
app = Eve()

@app.route('/qr/<regex("[a-f0-9]{24}"):item_id>')
def qr(item_id):
    data = qrcode.make(item_id)
    return "asdasdasd"

def add_qr_code(*args, **kwargs):
    print(args)
    print(kwargs)
    return []

if __name__ == '__main__':
    app.on_fetched_item_boxes += add_qr_code
    app.on_fetched_resource_boxes += add_qr_code
    # app.on_post_POST_boxes += add_qr_code
    app.run()