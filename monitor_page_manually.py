import time

from config import client, collection, publish_ready, published
from post_to_markdown import update_row

def row_callback(record, changes):
    start = record.status
    if start == publish_ready:
        record.status = published
        print("Updating", end=' ')
        print(record.title, "...", sep="")
        update_row(record)
        print("Done!\n")
    time.sleep(3)

def register_row_callbacks(collection):
    print("Registering Row Callbacks...\n")
    rows = collection.get_rows()
    for row in rows:
        row.add_callback(row_callback, callback_id="row_callback")
    return

def collection_callback(record, difference, changes):
    register_row_callbacks(record)

if __name__ == "__main__":
    collection.add_callback(collection_callback)
    register_row_callbacks(collection)
    while True:
        client.start_monitoring()
        time.sleep(0.01)
