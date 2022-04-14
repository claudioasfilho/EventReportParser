#Raw UART BGAPI Parser

This Code needs to be fed with an exported file from Saleae Logic Analyzer containing raw UART data (run.csv) from BGAPI Transaction.

It will Check for an Event Header and separate the events in different Messages, exporting two files, all the events and the remainder of

raw data. If the Raw data doesn't contain any "open-ended" Events then it means all the events were successfully transmitted by the NCP device.
