import json

with open("/home/susu/下载/c_question/prep_c_train_data/prep_c_train_data/data/tables.json", "r", encoding="utf-8") as f:
    tables_data = json.load(f)

with open("test_table.json", "w", encoding="utf-8") as f:
    json.dump(tables_data, f, indent=2, ensure_ascii=False)
    print("Done!")


 #"Table_f4824235453d11e9bd5ff40f24344a08":