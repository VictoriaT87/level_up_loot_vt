# **Local Development**

<br/>

**[Link to Deployed Site](https://levelup-loot-vt.herokuapp.com/)**

---
## **Deployment Steps**

**Create Repository**

This project was developed by forking the [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template).

1. Click the template link
2. Click use this template and create a new respository
3. Name the repository
4. Launch using the Gitpod web extension


**1. Create a requirements.txt file**

In the terminal, enter the command 'pip3 freeze > requirements.txt'. This creates our requirements.txt file which will be read by Heroku.

**2. Create an external database on ElephantSQL.com**

* Go to [ElephantSQL.com](https://www.elephantsql.com/) and click *Get a managed database today* button.
* Select Tiny Turtle by pressing the *Try now for FREE* button
* Select *Log in with GitHub* and authorize ElephantSQL with your selected GitHub account
* Click *Create New Instance*

After logging in to ElephantSQL:
* Set up your plan
    * Give your plan a **Name** (This is commonly the name of the project)
    * Select *Select Region*
    * Select a region and data center (Choose the one closest to you)
    * Click *Review*
    * Check that your details are correct and then click *Create New Instance*
    * Return to the dashboard and click on the *database instance name*
    * Copy the database url

**3. Set up Heroku**
* Go to [Heroku.com](https://www.heroku.com/) and log in
* Choose the New button and from the dropdown, select *Create new app*
* Add your preferred app name and select your location and click the create app button
* Add a Config Var **DATABASE_URL** and paste your ElephantSQL database URL in as the value

**4. Connect the external database to GitPod**
* In an env.py file on your repository, add the **DATABASE_URL** and give it the value of the copied database URL <br/>
```bash
os.environ.setdefault("DATABASE_URL", "the_copied_database_url")
```
* Install **dj-database-url** and **psycopg2**:
```bash
pip3 install dj_database_url==0.5.0 psycopg2
```
* Add both to your **requirements.txt** file:
```bash
pip3 freeze --local > requirements.txt
```
* In **settings.py** file, import **dj_database_url**:
```python
import os
import dj_database_url
```
* Replace the **DATABASE_URL** environment variable:
```python
if "DATABASE_URL" in os.environ:
    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```

* Run the migrate command in the terminal
```bash
python3 manage.py migrate
```
* Create a superuser for your new database
```bash
python3 manage.py createsuperuser
```
Follow the steps to create your superuser username and password.

**5. Fixtures**
To load fixtures into your project:

* Use **loaddata** to upload the products JSON file by running:
```bash
python3 manage.py loaddata products.json
```

**6. Deploying to Heroku**
* Install **gunicorn** and freeze into **requirements.txt**
```bash
pip3 install gunicorn
pip3 freeze > requirements.txt
```
* Create a **Procfile** in the root directory for Heroku to read:
```Procfile
web: gunicorn level_up_loot.wsgi:application
```
* Temporarily disable **collectstatic** by logging into the Heroku CLI in the terminal or on Heroku.com and set DISABLE_COLLECTSTATIC to 1:
```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name
```
* Add the hostname of the Heroku app to allowed hosts in **settings.py**:
```python
ALLOWED_HOSTS = ['deployed-site-url', 'localhost']
```
* Save the **settings.py** file, and add and commit the changes:
```python
git push Heroku main
```

* To enable automatic deploys on Heroku, go to the app in Heroku. On the deploy tab, connect to GitHub. Search for the repository and then click *connect*. Then click *Enable Automatic Deploys*.

**8. Generate SECRET_KEY**
1. Django creates a Secret Key for each project upon creation. Unless you immediately added this to your env.py file, the key may now be compromised. We can create a new one with the link below.
2. Go to [miniwebtool's Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/), click on the *Generate Django Secret Key* button and copy the value.
4. In Heroku, add a new Config Var **SECRET_KEY** and give it the value of the newly generated secret key and then click *add*.
5. In the **settings.py** file add:
```python
SECRET_KEY = os.environ.get('SECRET_KEY', '')
```
6. Change the **DEBUG**
```python
DEBUG = 'DEVELOPMENT' in os.environ
```
Save the **settings.py** file, add, commit and then git push these changes.

**9. Set up Amazon Web Services' S3 to host static files and images**
**Create an account** <br/>
* Create an AWS Account by going to [aws.amazon.com](https://aws.amazon.com/) and click on *create an aws account*
* Complete the verification and once you confirm all the required information, your account will be created.
**Create a bucket**
- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

  ```shell
  [
  	{
  		"AllowedHeaders": [
  			"Authorization"
  		],
  		"AllowedMethods": [
  			"GET"
  		],
  		"AllowedOrigins": [
  			"*"
  		],
  		"ExposeHeaders": []
  	}
  ]
  ```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
- Policy Type: **S3 Bucket Policy**
- Effect: **Allow**
- Principal: `*`
- Actions: **GetObject**
- Amazon Resource Name (ARN): **paste-your-ARN-here**
- Click **Add Statement**
- Click **Generate Policy**
- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

  ```shell
  {
  	"Id": "Policy1234567890",
  	"Version": "2012-10-17",
  	"Statement": [
  		{
  			"Sid": "Stmt1234567890",
  			"Action": [
  				"s3:GetObject"
  			],
  			"Effect": "Allow",
  			"Resource": "arn:aws:s3:::your-bucket-name/*"
  			"Principal": "*",
  		}
  	]
  }
  ```

- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
- Click **Save**.

- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).
- Download the CSV file with the secret keys.

**10. Connecting Django to S3**
* Install **boto3** and **django-storages**
```bash
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
* Add `storages` to the installed apps in **settings.py**
* Add the bucket configuration:
```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
* Add the Secret Keys from the downloaded CSV file to Heroku:
| AWS_ACCESS_KEY_ID | 
| AWS_SECRET_ACCESS_KEY |
| USE_AWS | True |
* Remove **COLLECTSTATIC** variable from the Config Vars
* Create **custom_storages.py** file and add:
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
* In **settings.py**, set the static locations as follows.
```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
* Git add . and git push to save these changes.
* Go to s3 and create a new folder called media then click *upload*. Add the product images files, click *next* and under manage public permissions, select *grant public read access to these objects.* Then click *next* through to the end and finally, click *upload*.

11. Setting  up Stripe
* Log in to Stripe, click the *developers* link, and then *API Keys*
* Add them as Config Vars in Heroku
* Create a new webhook endpoint in the developer's menu by clicking *add endpoint*.
* Add the URL for our Heroku app, followed by /checkout/WH and select *receive all events and add endpoint*.
* Add the webhooks signing secret to the Heroku config variables.

---
## How to Fork the repository
  - On GitHub.com, navigate to the repository.
  - In the top-right corner of the page, click Fork.
  - Select an owner for the forked repository.
  - By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
  - Optionally, add a description of your fork.
  - Choose whether to copy only the default branch or all branches to the new fork.
  - Click Create fork.

---
## How to Clone the repository
  - On GitHub.com, navigate to the repository.
  - Above the list of files, click the Code button.
  - Copy the URL for the repository.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
  - Press Enter. Your local clone will be created.
