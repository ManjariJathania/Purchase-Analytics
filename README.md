# Purchase-Analytics

Note: As github's file size limit is 100 MB I haven't uploaded the data file but [here](https://s3.amazonaws.com/instacart-datasets/instacart_online_grocery_shopping_2017_05_01.tar.gz?X-Amz-Expires=21600&X-Amz-Date=20190408T210151Z&X-Amz-Security-Token=FQoGZXIvYXdzEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDC5DCZuQhVAbtADLryKVBAVcqFkUb71wqnkE45KiFORTCDvNbpAT7Ls9JiI75P8xe8O5hWrdKI1iUG%2BEmMoo7MAYzOeV%2F85AYShTD592OFf3dA0VOgfk1CUt3R2TdNGmfFt%2FcNBC1XAFAlQTET598L3kgvog2JMV5LfuRogvu8StW9irXNII7GkUE0bddZn70LLmQRpGTqu7XoZ8BtPHLu4OQJ5kexWe0oX3OqmiuTdqiWpvUfJNeaBw4vMQGZR%2FGM8Dmsnd%2FFqeFEi%2Bx3z0Wxu6AR1E36pGsBhvbdnTHU%2FIlIpDmlAUO%2F%2FgzdvSVMcSljfMkjQaT3VEZ1ESylrONz9a2LqhwtUPjOIlVLrGMfAmU%2BBxQtAESl12Rhhw17J3YV3oGa5dQWIZ9zzzmkzCs82KatVQaQhLKkmGTDlz%2BSw12rsewMyYI3%2Bcudls8YL1eYquG9CyqQZBDsBxLFDpBfsJpEUx5HjiVXMbEiTPc2I5SAje7EJFYrDehZQQuT8H%2Bt5OMd937uv17G0VC6i1U9U3hpYbGai0C5LXwEyFjCHg9trDQgS%2BovKNTEw3ydunJIQD1PAgJwdPA2NetsKI4o9C99yXA1eI4B%2FnDmhwqfDy7HEvPK%2Fv5yTQTq14RUCuN2B%2FcJ%2F9q8DiNA85lLje0D20MHCK35miJDFDXEOTQvq8gH8%2BudfzmgjMl0haGnBLLXlyBh%2F4Panh3NJh1LuJ8lTJaJYUKKzdruUF&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASDAVXBX75OGCOX4U%2F20190408%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=2bbfdbde7f8ad2f8cfe30c2abc469a0547599d2f0e645d62e40c321b8853214b) is the link for it to download.

Instructions to run and test the code with original data.

1.  Open command prompt.
2.  Go to Purchase-Analytics folder.
3.	Enter "run.sh"
4.	A window will pop up. Enter 1 to test the original data.(Before doing this make sure you have copied the 500MB file into ./input folder named as 
	"order_products.csv".)
5.	After the program finished, you will see a file named report.csv generated in the ./output folder.



Instructions to run and test the code with test data's.

For data in test_1 folder

1.  Open command prompt.
2.  Go to Purchase-Analytics/insight_testsuite folder.
3.	Enter "run_test.sh"
4.	A window will pop up. Enter 2 to test the data in ./test_1/input folder.(This folder already contains the test data but you are most welcome to
	change this data at any point of time with the same format.)
5.	After the program is finished, you will see the final result on screen as well as a file named report.csv is generated in the ./test_1/output folder.


For data in your-own-test_1 folder

1.  Open command prompt.
2.  Go to Purchase-Analytics/insight_testsuite folder.
3.	Enter "run_test.sh"
4.	A window will pop up. Enter 3 to test the data in ./your-own-test_1/input folder.(This folder already contains the test data but you are most
	welcome to change this data at any point of time with the same format.)
5.	After the program is finished, you will see the final result on screen as well as a file named report.csv is generated in the ./your-own-test_1/output folder.