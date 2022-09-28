import yuritasks as yuri

yuri.do.var("source_path", "PUT_HERE_SOME_GIT_PATH")


@yuri.task
def myproject_commit_source(_args):
    yuri.do.cd("$source_path")\
        .run("git add -A")\
        .run_with_input("git coomit -m {i}", "Commit changes: ")\
        .run("git pull")\
        .run("git push -u origin main")


if __name__ == "__main__":
    yuri.run()
