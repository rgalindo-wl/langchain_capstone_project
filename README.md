# Langchain capstone project

Capstone project for Wizeline Langchain sprint

By: Roberto Galindo

This project implements RAG capability, which is available through an API. The main idea is to enable the user with an interface to allow query PDF documents to search for quick answers covered on the file.

The best use case for this application is getting quick responses to questions that an agent that has read a document with deep technical information can respond. So if you are interested into know a specifc information you can query (with natural language questions) PDF files from research papers, package manuals, books or any other long document.




## Project Structure
```bash
.
├── data            
│   ├── final                       # data after training the model
│   └── raw                         # raw data
├── .env.example                    # copy to store secrets
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # commands to set up the environment
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # Poetry dependencies
├── README.md                       
├── src                             # Main source code
└── tests                           # Tests code
```

## Getting started

### Before you start

- Get sure you have `python` with a version `>=3.8`, if you want to start from fresh take a look at [this resource](https://wiki.python.org/moin/BeginnersGuide/Download).
- Make sure having `make` installed. You can check [the GNU Make](https://www.gnu.org/software/make/#download)
- Install `poetry` by following the reccomended instructions in [the oficial documentation](https://python-poetry.org/docs/#installation)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Running the project

There is a simple way to startup from a fresh download/clone, just follow these steps

**Quick deploy**

To install all the project just run:

```bash
make
make conf
```
 
Once the `.env` file is created, make sure to set the required `OPENAI_API_KEY` using a valid key _i.e._:

```
OPENAI_API_KEY=secret-token-key
```

At this point the service will be available by running:

```bash
make api
```

Now you can get access to the API swagger using [http://localhost:8000/docs](http://localhost:8000/docs). Then test it by following the next steps:

1. Open the POST `/upload_files` endpoint to test the API.
2. Click on **Try it out** button.
3. Choose a `project_name` value _i.e._ `test`.
4. Write a question in the `quetion` field.
5. Click on **Add string item** to enable the option to choose file from you computer
   - Click on the button **Choose File**
   - Use the file browser window that was opened to select a PDF file you want to query, then click on **Open**
   - If you want to have more context, repeat from _5_ to select other file
6. When you selected the file(s), the question, and the project name, you can click on **Execute** button to run the RAG function.
7. Enjoy



### Dev hints (contribute)


To install all the dependencies of this project use

```bash
poetry install
```

To install any other dependency type

```bash
poetry add <package-name>[@<version>]
```

## Contact info

[Roberto Galindo](mailto:roberto.galindo@wizeline.com)
