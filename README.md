# Starter Project

This is a simple starter project for rest api application using flask and sqlite tech stack. 

Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


# Populate database
From project folder run:
```
py db/seed.py
```

# Running the app
```
flask run --debug
```

# Environment variables
Please define environment variable as following:\
JWT_SECRET=somesecret

# REST Client
Rest client for testing the endpoint available at folder:
```
test/test.http
```

Please install [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension for VS Code.

In test.http file check for this endpoint http://localhost:5000/auth to get the access token.
