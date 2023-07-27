from os import listdir, mkdir
from shutil import rmtree

from jinja2 import Environment, FileSystemLoader

indir = "templates"
outdir = "output"
outjournal = f"{outdir}/journal"

environment = Environment(loader=FileSystemLoader(indir))

contents = listdir(indir)
print("+++ rendering top level templates")
for file in contents:
    if not file.endswith(".html") or file == "base.html":
        continue

    template = environment.get_template(file)

    with open(f"{outdir}/{file}", mode="w", encoding="utf-8") as results:
        results.write(template.render())
        print(f"... wrote {outdir}{file}")

print("+++ rendering journal entries")
contents = listdir(f"{indir}/journal")

rmtree(outjournal, ignore_errors=True)
mkdir(outjournal)
for file in contents:
    if not file.endswith(".html"):
        continue

    template = environment.get_template(f"journal/{file}")

    with open(f"{outjournal}/{file}", mode="w", encoding="utf-8") as results:
        results.write(template.render())
        print(f"... wrote {outjournal}{file}")
