---
sourceFile: "Mocking API services in development and testing with WireMock | Docker Docs"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.661Z"
---

# Mocking API services in development and testing with WireMock | Docker Docs

2a325944-7f6a-49e5-bc08-d2a7f288c891

Mocking API services in development and testing with WireMock | Docker Docs

eec20b3c-691f-424f-8454-34e7fd65ca74

https://docs.docker.com/guides/wiremock/

Mocking API services in development and testing with WireMock | Docker Docs

Insights on the state of AI agents from 800+ builders and leaders. Download your copy

https://www.docker.com/resources/the-state-of-agentic-ai-white-paper/

https://docs.docker.com/

Get started

https://docs.docker.com/get-started/

https://docs.docker.com/guides/

https://docs.docker.com/manuals/

https://docs.docker.com/reference/

Gordon, your AI assistant for Docker docs

Start a new chat

What can I help you with?

I'm Gordon, your AI assistant for Docker and documentation questions.

Get started with Docker

Docker Hardened Images

MCP Toolkit

Create an org

When enabled, Gordon considers the current page you're viewing to provide more relevant answers.

Share feedback

https://github.com/docker/docs/issues/23966

Answers are generated based on the documentation.

https://docs.docker.com/guides/

Get started

https://docs.docker.com/get-started/

https://docs.docker.com/manuals/

https://docs.docker.com/reference/

Mocking API services in development and testing with WireMock

https://docs.docker.com/guides/wiremock/

Mocking API services in development and testing with WireMock

JavaScript App development Distributed systems

« Back to all guides

https://docs.docker.com/guides/

https://docs.docker.com/

https://docs.docker.com/guides/

/ Mocking API services with WireMock

Mocking API services in development and testing with WireMock

Ask Gordon Copy Markdown View Markdown

Table of contents

Using WireMock with Docker

https://docs.docker.com/guides/wiremock/#using-wiremock-with-docker

Prerequisites

https://docs.docker.com/guides/wiremock/#prerequisites

Launching WireMock

https://docs.docker.com/guides/wiremock/#launching-wiremock

Using WireMock in development

https://docs.docker.com/guides/wiremock/#using-wiremock-in-development

Use mock data in local development

https://docs.docker.com/guides/wiremock/#use-mock-data-in-local-development

Prerequisite

https://docs.docker.com/guides/wiremock/#prerequisite

Use a Live API in production to fetch real-time weather data from AccuWeather

https://docs.docker.com/guides/wiremock/#use-a-live-api-in-production-to-fetch-real-time-weather-data-from-accuweather

https://docs.docker.com/guides/wiremock/#recap

During local development and testing, it's quite common to encounter situations where your app is dependent on the remote APIs. Network issues, rate limits, or even downtime of the API provider can halt your progress. This can significantly hinder your productivity and make testing more challenging. This is where WireMock comes into play.

WireMock is an open-source tool that helps developers to create a mock server that simulates the behavior of real APIs, providing a controlled environment for development and testing.

Imagine you have both an API and a frontend app, and you want to test how the frontend interacts with the API. Using WireMock, you can set up a mock server to simulate the API's responses, allowing you to test the frontend behavior without relying on the actual API. This can be particularly helpful when the API is still under development or when you want to test different scenarios without affecting the actual API. WireMock supports both HTTP and HTTPS protocols and can simulate various response scenarios, including delays, errors, and different HTTP status codes.

#### In this guide, you'll learn how to:

Use Docker to launch up a WireMock container.

Use mock data in the local development without relying on an external API

Use a Live API in production to fetch real-time weather data from AccuWeather.

Using WireMock with Docker

https://docs.docker.com/guides/wiremock/#using-wiremock-with-docker

The official

Docker image for WireMock

https://hub.docker.com/r/wiremock/wiremock

provides a convenient way to deploy and manage WireMock instances. WireMock is available for various CPU architectures, including amd64, armv7, and armv8, ensuring compatibility with different devices and platforms. You can learn more about WireMock standalone on the

WireMock docs site

https://wiremock.org/docs/standalone/docker/

Prerequisites

https://docs.docker.com/guides/wiremock/#prerequisites

The following prerequisites are required to follow along with this how-to guide:

Docker Desktop

https://www.docker.com/products/docker-desktop/

Launching WireMock

https://docs.docker.com/guides/wiremock/#launching-wiremock

#### Launch a quick demo of WireMock by using the following steps:

GitHub repository

https://github.com/dockersamples/wiremock-node-docker

$ git clone https://github.com/dockersamples/wiremock-node-docker

Navigate to the

wiremock-endpoint

$ cd wiremock-node-docker/

WireMock acts as the mock API that your backend will communicate with to retrieve data. The mock API responses have already been created for you in the mappings directory.

3. Start the Compose stack by running the following command at the root of the cloned project directory

$ docker compose up -d

After a moment, the application will be up and running.

You can check the logs by selecting the

wiremock-node-docker

4. Test the Mock API.

$ curl http://localhost:8080/api/v1/getWeather\?city\=Bengaluru

#### It will return the following canned response with mock data:

{"city":"Bengaluru","temperature":27.1,"conditions":"Mostly cloudy","forecasts":\[{"date":"2024-09-02T07:00:00+05:30","temperature":83,"conditions":"Partly sunny w/ t-storms"},{"date":"2024-09-03T07:00:00+05:30","temperature":83,"conditions":"Thunderstorms"},{"date":"2024-09-04T07:00:00+05:30","temperature":83,"conditions":"Intermittent clouds"},{"date":"2024-09-05T07:00:00+05:30","temperature":82,"conditions":"Dreary"},{"date":"2024-09-06T07:00:00+05:30","temperature":82,"conditions":"Dreary"}\]}

With WireMock, you define canned responses using mapping files. For this request, the mock data is defined in the JSON file at

wiremock-endpoint/mappings/getWeather/getWeatherBengaluru.json

. For more information about stubbing canned responses, refer to the

WireMock documentation

https://wiremock.org/docs/stubbing/

Using WireMock in development

https://docs.docker.com/guides/wiremock/#using-wiremock-in-development

Now that you have tried WireMock, let's use it in development and testing. In this example, you will use a sample application that has a Node.js backend. This app stack has the following configuration:

Local Development Environment: The context in which the Node.js backend and WireMock are running.

Node.js Backend: Represents the backend application that handles HTTP requests.

External AccuWeather API: The real API from which live weather data is fetched.

WireMock: The mock server that simulates the API responses during testing. It runs as a Docker container.

In development, the Node.js backend sends a request to WireMock instead of the actual AccuWeather API.

In production, it connects directly to the live AccuWeather API for real data.

Use mock data in local development

https://docs.docker.com/guides/wiremock/#use-mock-data-in-local-development

Let's set up a Node app to send requests to the WireMock container instead of the actual AccuWeather API.

Prerequisite

https://docs.docker.com/guides/wiremock/#prerequisite

Node.js and npm

https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

Ensure that WireMock container is up and running (see

Launching Wiremock

https://docs.docker.com/guides/wiremock/#launching-wiremock

#### Follow the steps to setup a non-containerized Node application:

Navigate to the

accuweather-api

directory Make sure you're in the directory where your

package.json

file is located.

Set the environment variable. Open

file placed under

accuweather-api/

directory. Remove the old entries and ensure that it just contains the following single line.

API\_ENDPOINT\_BASE=http://localhost:8080

This will tell your Node.js application to use the WireMock server for API calls.

3. Examine the Application Entry Point

The main file for the application is

, located in the

accuweather-api/src/api

This file starts the

getWeather.js

module, which is essential for your Node.js application. It uses the

package to load environment variables from the

Based on the value of

API\_ENDPOINT\_BASE

, the application routes requests either to the WireMock server (

http://localhost:8080

) or the AccuWeather API. In this setup, it uses the WireMock server.

The code ensures that the

ACCUWEATHER\_API\_KEY

is required only if the application is not using WireMock, enhancing efficiency and avoiding errors.

require("dotenv").config();

const express = require("express");
const axios = require("axios");

const router = express.Router();
const API\_ENDPOINT\_BASE = process.env.API\_ENDPOINT\_BASE;
const API\_KEY = process.env.ACCUWEATHER\_API\_KEY;

console.log('API\_ENDPOINT\_BASE:', API\_ENDPOINT\_BASE);  // Log after it's defined
console.log('ACCUWEATHER\_API\_KEY is set:', !!API\_KEY); // Log boolean instead of actual key

if (!API\_ENDPOINT\_BASE) {
  throw new Error("API\_ENDPOINT\_BASE is not defined in environment variables");
}

// Only check for API key if not using WireMock
if (API\_ENDPOINT\_BASE !== 'http://localhost:8080' && !API\_KEY) {
  throw new Error("ACCUWEATHER\_API\_KEY is not defined in environment variables");
}
// Function to fetch the location key for the city
async function fetchLocationKey(townName) {
  const { data: locationData } = await
axios.get(\`${API\_ENDPOINT\_BASE}/locations/v1/cities/search\`, {
    params: { q: townName, details: false, apikey: API\_KEY },
  });
  return locationData\[0\]?.Key;
}

Start the Node server Before you start the Node server, ensure that you have already installed the node packages listed in the package.json file by running

npm install

npm install 
npm run start

#### You should see the following output:

> express-api-starter@1.2.0 start
> node src/index.js

API\_ENDPOINT\_BASE: http://localhost:8080
..
Listening: http://localhost:5001

The output indicates that your Node application has successfully started. Keep this terminal window open.

5. Test the Mocked API Open a new terminal window and run the following command to test the mocked API:

$ curl "http://localhost:5001/api/v1/getWeather?city=Bengaluru"

#### You should see the following output:

{"city":"Bengaluru","temperature":27.1,"conditions":"Mostly cloudy","forecasts":\[{"date":"2024-09-02T07:00:00+05:30","temperature":83,"conditions":"Partly sunny w/ t-storms"},{"date":"2024-09-03T07:00:00+05:30","temperature":83,"conditions":"Thunderstorms"},{"date":"2024-09-04T07:00:00+05:30","temperature":83,"conditions":"Intermittent clouds"},{"date":"2024-09-05T07:00:00+05:30","temperature":82,"conditions":"Dreary"},{"date":"2024-09-06T07:00:00+05:30","temperature":82,"conditions":"Dreary"}\]}%

This indicates that your Node.js application is now successfully routing requests to the WireMock container and receiving the mocked responses You might have noticed that you're trying to use

http://localhost:5001

as the URL instead of port

. This is because your Node.js application is running on port

, and it's routing requests to the WireMock container that's listening on port

. Tip Before you proceed to the next step, ensure that you stop the node application service.

Use a Live API in production to fetch real-time weather data from AccuWeather

https://docs.docker.com/guides/wiremock/#use-a-live-api-in-production-to-fetch-real-time-weather-data-from-accuweather

To enhance your Node.js application with real-time weather data, you can seamlessly integrate the AccuWeather API. This section of the guide will walk you through the steps involved in setting up a non-containerized Node.js application and fetching weather information directly from the AccuWeather API.

Create an AccuWeather API Key Sign up for a free AccuWeather developer account at

https://developer.accuweather.com/

https://developer.accuweather.com/

. Within your account, create a new app by selecting

on the top navigation menu to get your unique API key.

AccuWeather API

https://developer.accuweather.com/

is a web API that provides real-time weather data and forecasts. Developers can use this API to integrate weather information into their applications, websites, or other projects.

Change directory to

accuweather-api

$ cd accuweather-api

Set your AccuWeather API key using the

file: Tip To prevent conflicts, ensure that any existing environment variables named

API\_ENDPOINT\_BASE

ACCUWEATHER\_API\_KEY

are removed before modifying the

file. Run the following command on your terminal:

unset API\_ENDPOINT\_BASE
unset ACCUWEATHER\_API\_KEY

It's time to set the environment variables in the

ACCUWEATHER\_API\_KEY=XXXXXX
API\_ENDPOINT\_BASE=http://dataservice.accuweather.com

Make sure to populate

ACCUWEATHER\_API\_KEY

with the correct value.

4. Install the dependencies Run the following command to install the required packages:

$ npm install

This will install all the packages listed in your

package.json

file. These packages are essential for the project to function correctly. If you encounter any warnings related to deprecated packages, you can ignore them for now for this demonstration.

5. Assuming that you don't have a pre-existing Node server running on your system, go ahead and start the Node server by running the following command:

$ npm run start

#### You should see the following output:

> express-api-starter@1.2.0 start
> node src/index.js

API\_ENDPOINT\_BASE: http://dataservice.accuweather.com
ACCUWEATHER\_API\_KEY is set: true 
Listening: http://localhost:5001

Keep this terminal window open.

6. Run the curl command to send a GET request to the server URL. In the new terminal window, enter the following command:

$ curl "http://localhost:5000/api/v1/getWeather?city=Bengaluru"

By running the command, you're essentially telling your local server to provide you with weather data for a city named

. The request is specifically targeting the

/api/v1/getWeather

endpoint, and you're providing the query parameter

city=Bengaluru

. Once you execute the command, the server processes this request, fetches the data and returns it as a response, which

will display in your terminal. When fetching data from the external AccuWeather API, you're interacting with live data that reflects the latest weather conditions.

https://docs.docker.com/guides/wiremock/#recap

This guide has walked you through setting up WireMock using Docker. You've learned how to create stubs to simulate API endpoints, allowing you to develop and test your application without relying on external services. By using WireMock, you can create reliable and consistent test environments, reproduce edge cases, and speed up your development workflow.

Edit this page

https://github.com/docker/docs/edit/main/content/guides/wiremock.md

Request changes

https://github.com/docker/docs/issues/new?template=doc\_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fguides%2fwiremock%2f&labels=status%2Ftriage

Table of contents

Using WireMock with Docker

https://docs.docker.com/guides/wiremock/#using-wiremock-with-docker

Prerequisites

https://docs.docker.com/guides/wiremock/#prerequisites

Launching WireMock

https://docs.docker.com/guides/wiremock/#launching-wiremock

Using WireMock in development

https://docs.docker.com/guides/wiremock/#using-wiremock-in-development

Use mock data in local development

https://docs.docker.com/guides/wiremock/#use-mock-data-in-local-development

Prerequisite

https://docs.docker.com/guides/wiremock/#prerequisite

Use a Live API in production to fetch real-time weather data from AccuWeather

https://docs.docker.com/guides/wiremock/#use-a-live-api-in-production-to-fetch-real-time-weather-data-from-accuweather

https://docs.docker.com/guides/wiremock/#recap

https://www.linkedin.com/company/docker

https://x.com/docker/

https://www.facebook.com/docker.run

http://www.youtube.com/user/dockerrun

https://www.instagram.com/dockerinc/

Product offerings

https://www.docker.com/

https://www.docker.com/pricing?ref=Docs&refAction=DocsFooter

https://www.docker.com/company/

https://docs.docker.com/llms.txt

llms-full.txt

https://docs.docker.com/llms-full.txt

Cookies Settings |

Terms of Service

https://www.docker.com/legal/docker-terms-service

https://www.dockerstatus.com/

https://www.docker.com/legal

Copyright © 2013-2026 Docker Inc. All rights reserved.

Search this site Results will appear as you type Clear

Start typing to search the documentation

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.

Cookies Settings Reject All Accept All Cookies

Privacy Preference Center

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.

More information

https://cookiepedia.co.uk/giving-consent-to-cookies

Manage Consent Preferences

Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

Cookie List

checkbox label label

Apply Cancel

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

Reject All Confirm My Choices

