- Got an understanding of how packages and modules are managed in python and the best practices associated.
- Solved hackerrank problems on `DefaultDict` and `OrderedDict ` methods.
- Created and Structured the Agent Development Kit as a proper Python package.
- ADK has two utils: 1. get_time 2. text_summarizer
- Project Structure:<br/>
```shell
adk/
├── agent/
│   ├── __init__.py
│   ├── .env
│   ├── agent.py
│   └── tools/
│       └── utils/
│           ├── get_time.py
│           ├── text_summarizer.py
└── .gitignore
  
```
- Proper modularization is followed to have clean agent code and minimize chances of error
- API keys are added in .env to avoid vulnerability and are not tracked by version control.
- The `.gitignore` file ensures sensitive files like `.env` and unnecessary files such as `__pycache__/` and other temporary files are excluded from git commits, keeping the repository clean and secure.