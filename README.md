# Open Gateway's SIM Swap API sample Python backend application

This sample app showcases how to use the Open Gateway SIM Swap API from a Python backend application. It uses the Telefónica's Open Gateway Sandbox as the testing environment exposing Open Gateway APIs. For additional information on the SIM Swap API, the Open Gateway initiative and Telefónica's resources for developers, please refer to the [parent repository](https://github.com/Telefonica/opengateway-samples-simswap).

## Overview

You will find three Python scripts to test the SIM Swap API consumption in the following ways:
- A command line script taking a phone number as an argument and using the Sandbox's SDK to check for recent SIM card swaps
- A version of the same script performing HTTP request instead of using the SDK
- A web server publishing a custom API for a [frontend application](https://github.com/Telefonica/opengateway-samples-simswap-frontend) to offer the SIM Swap functionality on a human interface

The following is a high level architecture diagram of the components involved in using Open Gateway APIs applied to this sample app. Note that Telefónica's Open Gateway Sandbox is used for this app as a testing environment, being the final scenario subscribing Open Gateway API products to an Open Gateway channel partner, also known as aggregators:

![High level architecture diagram](architecture.png)
*[Camara](https://camaraproject.org) is the Open Gateway API's standardization body*

*Aggregator is an Open Gateway channel partner. This sample app uses the Telefónica's Open Gateway Sandbox as a sandbox aggregator, both its API gateway and its Python SDK*

*The sample command line backend script is versioned both using the Sandbox SDK and performing HTTP requests to the Sandbox API gateway*

## Requirements

To clone and run the sample app scripts:
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)

To be able to use the Telefónica Open Gateway Sandbox and its SDK:
- Check how to know and join our programs to get credentials for your app [here](https://github.com/Telefonica/opengateway-samples-simswap)
- Install the [Sandbox's Python SDK](https://pypi.org/project/opengateway-sandbox-sdk/)

```Shell
pip install opengateway-sandbox-sdk
```

## Configuration

For the sake of simplicity, you will find the following values hardcoded in the scripts. Some of them need to be replaced with the actual values provided when registering your app in the Open Gateway Sandbox, or in your Open Gateway channel partner of choice:
- Your app credentials
	- `APP_CLIENT_ID` and `APP_CLIENT_SECRET`, as obtained from registration
- Your channel partner API exposure platform
	- `API_GATEWAY_URL`, Sandbox's API gateway URL is included
- The Open Gateway API product to use
	- `GRANT_TYPE`, leave it fixed for CIBA (check the [parent repository](https://github.com/Telefonica/opengateway-samples-simswap) for information on the authorization flows)
	- `PURPOSE`, leave it fixed for a fraud prevention use case (the one available for the SIM Swap API as an Open Gateway product)

On a production environment, **be sure to store these values in a secure way**, such as environment variables or a configuration file.