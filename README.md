# Pension

This project is to monitor the value of a NEST pension. 

The script will:
1. Open a browser and navigate to the NEST pension website
2. Login as a specified user
3. Obtain the current value of the pension pot, including the "Number of units", "Unit Price" and "Fund value"
4. These values are then passed into a webhook to be recorded in a spreadsheet 

For the webhook, I have used ifttt with "Webhooks" as a trigger.
Webhooks receives a web request and appends these values along with the current date and time to a google spreadsheet:
> {{OccurredAt}} ||| {{Value1}} ||| {{Value2}} ||| {{Value3}}
