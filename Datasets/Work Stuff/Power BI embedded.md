To embed power bi content, must develop app to acquire an access token.

Azure AD token:
- **Azure AD token must be present in all API operations**
- App uses **interactive authentication flow** for organizational use (prompt SSO)
- App should cache the Azure AD token, to use Power BI content with correct permissions
- Can either use a Service Principal or Master User account to acquire Azure AD token
	- Master account is best suited for dev/test apps or apps that need write permissions
	- **Service Principal account is the Recommended** method 