import tkinter as tk

# Exchange rates data (as provided)
exchange_rates = {"USD":1,"AED":3.67,"AFN":73.58,"ALL":100.54,"AMD":385.86,"ANG":1.79,"AOA":833.74,"ARS":349.98,"AUD":1.57,"AWG":1.79,"AZN":1.7,"BAM":1.83,"BBD":2,"BDT":109.77,"BGN":1.83,"BHD":0.376,"BIF":2822.4,"BMD":1,"BND":1.36,"BOB":6.93,"BRL":4.98,"BSD":1,"BTN":83.05,"BWP":13.77,"BYN":2.93,"BZD":2,"CAD":1.36,"CDF":2327.89,"CHF":0.892,"CLP":881.1,"CNY":7.35,"COP":4072.66,"CRC":535.94,"CUP":24,"CVE":103,"CZK":22.79,"DJF":177.72,"DKK":6.97,"DOP":56.77,"DZD":137.05,"EGP":30.9,"ERN":15,"ETB":55.1,"EUR":0.934,"FJD":2.27,"FKP":0.802,"FOK":6.97,"GBP":0.802,"GEL":2.62,"GGP":0.802,"GHS":11.46,"GIP":0.802,"GMD":64.11,"GNF":8576.64,"GTQ":7.87,"GYD":209.24,"HKD":7.84,"HNL":24.63,"HRK":7.04,"HTG":136.22,"HUF":360.22,"IDR":15344.62,"ILS":3.85,"IMP":0.802,"INR":83.05,"IQD":1311.4,"IRR":41955.85,"ISK":134.08,"JEP":0.802,"JMD":154.68,"JOD":0.709,"JPY":147.63,"KES":146.62,"KGS":88.14,"KHR":4162.3,"KID":1.57,"KMF":459.55,"KRW":1335.31,"KWD":0.308,"KYD":0.833,"KZT":464.89,"LAK":19416.46,"LBP":15000,"LKR":321.83,"LRD":190.08,"LSL":19.12,"LYD":4.85,"MAD":10.17,"MDL":17.86,"MGA":4494.65,"MKD":57.46,"MMK":2099.61,"MNT":3507.74,"MOP":8.08,"MRU":38.2,"MUR":45.08,"MVR":15.45,"MWK":1099.44,"MXN":17.6,"MYR":4.68,"MZN":63.89,"NAD":19.12,"NGN":754.12,"NIO":36.59,"NOK":10.68,"NPR":132.88,"NZD":1.7,"OMR":0.384,"PAB":1,"PEN":3.7,"PGK":3.63,"PHP":56.73,"PKR":307.56,"PLN":4.31,"PYG":7303.92,"QAR":3.64,"RON":4.63,"RSD":109.38,"RUB":98.33,"RWF":1236.56,"SAR":3.75,"SBD":8.48,"SCR":12.99,"SDG":562.12,"SEK":11.12,"SGD":1.36,"SHP":0.802,"SLE":21.9,"SLL":21898.13,"SOS":569.25,"SRD":38.17,"SSP":1009.32,"STN":22.89,"SYP":12934.5,"SZL":19.12,"THB":35.54,"TJS":10.94,"TMT":3.5,"TND":3.13,"TOP":2.37,"TRY":26.85,"TTD":6.75,"TVD":1.57,"TWD":32.09,"TZS":2506.2,"UAH":36.93,"UGX":3735.72,"UYU":37.83,"UZS":12096.23,"VES":33.34,"VND":24078.09,"VUV":122.18,"WST":2.78,"XAF":612.74,"XCD":2.7,"XDR":0.757,"XOF":612.74,"XPF":111.47,"YER":250.25,"ZAR":19.12,"ZMW":20.78,"ZWL":4649.44}

# Create a function to convert currency
def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    if from_currency == to_currency:
        converted_amount.set(amount)
    else:
        try:
            exchange_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
            converted = amount * exchange_rate
            converted_amount.set(round(converted, 2))
        except KeyError:
            converted_amount.set("Currency not found in the exchange rates data.")

# Create the main application window
app = tk.Tk()
app.title("Currency Converter")

# Create input fields and labels
label_amount = tk.Label(app, text="Amount:")
label_from_currency = tk.Label(app, text="From Currency:")
label_to_currency = tk.Label(app, text="To Currency:")
label_result = tk.Label(app, text="Result:")

entry_amount = tk.Entry(app)
converted_amount = tk.StringVar()
result_label = tk.Label(app, textvariable=converted_amount)

# Create currency selection dropdowns
currencies = list(exchange_rates.keys())
combo_from_currency = tk.StringVar()
combo_from_currency.set(currencies[0])
combo_to_currency = tk.StringVar()
combo_to_currency.set(currencies[1])

from_currency_menu = tk.OptionMenu(app, combo_from_currency, *currencies)
to_currency_menu = tk.OptionMenu(app, combo_to_currency, *currencies)

# Create a "Convert" button
convert_button = tk.Button(app, text="Convert", command=convert_currency)

# Grid layout for widgets
label_amount.grid(row=0, column=0, padx=10, pady=10)
label_from_currency.grid(row=1, column=0, padx=10, pady=10)
label_to_currency.grid(row=2, column=0, padx=10, pady=10)
label_result.grid(row=3, column=0, padx=10, pady=10)

entry_amount.grid(row=0, column=1, padx=10, pady=10)
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)
result_label.grid(row=3, column=1, padx=10, pady=10)

convert_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
app.mainloop()
