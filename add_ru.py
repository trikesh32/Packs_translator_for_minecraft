from googletrans import Translator
import zipfile
import os
import json

translator = Translator(service_urls=[
    'translate.google.com'])

for f in os.listdir():
    if f.endswith(".jar") and zipfile.is_zipfile(f):
        with zipfile.ZipFile(f, "a", compression=zipfile.ZIP_DEFLATED) as zipf:
            if "assets/" in zipf.namelist():
                if len(list(zipfile.Path(f, "assets/").iterdir())) != 0 and f"assets/{list(zipfile.Path(f, 'assets/').iterdir())[0].name}/lang/ru_ru.json" not in zipf.namelist() and f"assets/{list(zipfile.Path(f, 'assets/').iterdir())[0].name}/lang/en_us.json" in zipf.namelist():
                    print("Working with " + f + "....")
                    s = zipf.open(f"assets/{list(zipfile.Path(f, 'assets/').iterdir())[0].name}/lang/en_us.json").read()
                    if b"\\'" in s:
                        s = s.replace(b"\\'", b"\'")
                    orig_map = json.loads(s)
                    new_map = {}
                    for k in orig_map.keys():
                        new_map[k] = "" if len(orig_map[k]) == 0 else translator.translate(orig_map[k], src="en",dest="ru").text
                        print(k)
                    zipf.writestr(f"assets/{list(zipfile.Path(f, 'assets/').iterdir())[0].name}/lang/ru_ru.json", json.dumps(new_map, ensure_ascii=0).encode("utf8"))
                else:
                    print(f + " skip")
            else:
                print(f + " skip")




