# Manus CMS

Open-Source content management system based on Django framework that you can use as an alternative to WordPress. The key difference in Manus CMS is that it is not bloated with so many useless plugins which don't do anything useful for your web application.
You can aslo set this up as easily as WordPress!

## How to Start Manus

First of all, you need `Python3` and `Node.js` installed on your system...

#### Linux

```bash
pip3 install virtualenv
virtualenv env
source env/bin/activate
python -m pip install -r requirements.txt
npm install
npm run dev
```

#### Windows

```bash
pip install virtualenv
virtualenv env
.\env\Scripts\activate
python -m pip install -r requirements.txt
npm install
npm run dev
```

### Contributions

We are now growing our application to be completed and we need your contributions to exist in this area. So if you have any idea to improve code quality I'm so happy to hear from you at [hasanparasteh@gmail.com](mailto:hasanparasteh@gmail.com).

**Before writing any code please be aware of `pre-commit` configs. It checks your code and format it with `black` before each commit! to configure it for your device just run `pre-commit install` on your terminal.**

### Todo

- compelete blogging platform
- refactor all the code base part by part
- re-create the pages application to make it more dynamic
