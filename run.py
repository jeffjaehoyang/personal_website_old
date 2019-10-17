import sys
from flaskblog import freezer, create_app

app = create_app()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)

    