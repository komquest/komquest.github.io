# Purpose: When attempting in place upgrade to 1909, 2004, 20H2 you get the message:

```bash
Setup has failed to validate the product key
```

## Attempted Fixes

https://superuser.com/questions/947130/windows-10-setup-has-failed-to-validate-the-product-key

```bash



I read through the log files in C:\$Windows.~BT and discovered an error message that said:

Unable to create temp file in C:\Users\me\AppData\Local\Temp. The file already exists.

(That's not the exact wording, but it's pretty close. I'm typing this on my other machine while watching the installer run.)

I ran Disk Cleanup on the drive, which cleared out the Temp folder and the downloaded/unpacked installer files (in C:\$Windows.~BT and C:\$Windows.~WS), then started the installer again and had no trouble.


```

##

https://www.thewindowsclub.com/windows-10-setup-failed-validate-product-key

```bash
Delete the temporary files. To do so, press Win + R and open the Run window and type temp. Press Enter to open the temporary files window and delete all the files.
Repeat the process with the Run commands %temp% and prefetch.

For domain-joined systems, remove them from the domain temporarily. A good reference to help with the same could be checked on Microsoft’s website here.
```

---

https://www.majorgeeks.com/content/page/windows_10_setup_has_failed_to_validate_the_product_key.html

```bash
If you were using the Media Creation Tool and purchased a retail key, there's an ESD folder on your C: drive. Open a Command-Prompt as Admin and browse to the ESD folder and type in the following replacing the x with your product key:
setup /pkey xxxxx-xxxxx-xxxxx-xxxxx-xxxxx


You'll need your Windows 10 ISO and a program to extract it to a folder. We recommend 7-Zip, PeaZip, or WinRar if you have it.
Extract the ISO to a folder. Open Notepad and type in the following:

[EditionID]
[Channel]
Retail
[VL]
0

Save this as ei.cfg in the Sources folder where you extracted the ISO. Be sure to select all files under Save as type. 

```

---

https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-edition-configuration-and-product-id-files--eicfg-and-pidtxt?view=windows-11

```bash

Save the files into the \Sources folder on the installation media. Windows Setup will use these files automatically during installation.

EI.cfg
[EditionID]
Enterprise
[Channel]
OEM
[VL]
0


PID.txt
[PID]
Value=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX


# Get Current Edition from ISO image after you mount it
DISM /Image:C:\Mount /Get-CurrentEdition

```

# The Fix:

- Make sure you move your Computers to an OU that doesn't inherrit policy and has no gpos, some GPOs break windows upgrade!!! 
