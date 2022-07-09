import uvicorn
"""Use to run app locally for development. Call app directly in production"""


def configure():
    """Not implemented. Intended for config when run as service in production"""
    # Todo: delete if not required
    pass


if __name__ == "__main__":
    configure()
    uvicorn.run("server.app:app", host="127.0.0.1", port=8000, reload=True)
else:
    configure()
