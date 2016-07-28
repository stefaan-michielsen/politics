
wage = {}

result = open("bediende.txt", "w")

for loon in range(0, 50000, 10):

    h = """curl 'http://www.sd.be/websvc2/Vacature/Tools/BrutoNetto/BrutoNetto.aspx' -H 'Cookie: ASP.NET_SessionId=d3tvlf55dlors3jcy0kpvd3u; lng=NL' -H 'Origin: http://www.sd.be' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: nl-NL,nl;q=0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: http://www.sd.be/websvc2/Vacature/Tools/BrutoNetto/BrutoNetto.aspx' -H 'Connection: keep-alive' --data '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTIwODQ5MTQwMzYPFgIeD1dpemFyZC5TdGF0ZUJhZxcAFgQCAQ8WAh4JaW5uZXJodG1sBQ1Mb29uc2ltdWxhdGllZAIFD2QWAgIBD2QWAmYPZBYGZg8WAh4HVmlzaWJsZWgWAmYPDxYCHgRUZXh0BSVFciB3ZXJkZW4gb25nZWxkaWdlIGdlZ2V2ZW5zIGluZ2V2dWxkZGQCBg9kFh4CEQ8QDxYKHgpEYXRhTWVtYmVyBQpQQVJBTUVURVJTHg5EYXRhVmFsdWVGaWVsZAUEQ09ERR4NRGF0YVRleHRGaWVsZAUMT01TQ0hfTUlEREVMHgtfIURhdGFCb3VuZGceDVNlbGVjdGVkVmFsdWUFAjAxZBAVABUAFCsDABYAZAIVDxAPFgIfAwUkV2Vya25lbWVyIHdvb250IGluIGhldCBWbGFhbXMgZ2V3ZXN0ZGRkZAIXDxAPFgIfAwUZV2Vya25lbWVyIGlzIG1pbmRlcnZhbGlkZWRkZGQCHw8QDxYKHwQFClBBUkFNRVRFUlMfBQUEQ09ERR8GBQpPTVNDSF9MQU5HHwdnHwgFAjk5ZBAVABUAFCsDABYAZAIjDxAPFgIfAwUXUGFydG5lciBpcyBtaW5kZXJ2YWxpZGVkZGRkAksPEGQPFgJmAgEWAgUIQXJiZWlkZXIFCEJlZGllbmRlZGQCTw8QDxYCHwMFE0pvbmdlciBkYW4gMTkgamFhcglkZGRkAlMPEA8WCh8EBQpQQVJBTUVURVJTHwUFBENPREUfBgUMT01TQ0hfTUlEREVMHwdnHwgFATBkEBUAFQAUKwMAFgBkAnEPDxYCHwMFAk9mZGQChQEPZBYCAgMPEGQPFgJmAgEWAhAFEE9wZW5iYWFyIHZlcnZvZXIFAk9WZxAFDlByaXbDqS12ZXJ2b2VyBQJQVmdkZAKZAQ9kFgICAw9kFgICFQ8QDxYIHwQFClBBUkFNRVRFUlMfBQUEQ09ERR8GBQxPTVNDSF9NSURERUwfB2dkEBUAFQAUKwMAFgBkArsBDw8WAh8DBQ5CcnV0byA9PiBuZXR0b2RkAr0BDw8WAh8DBQ5OZXR0byA9PiBicnV0b2RkAr8BDw8WAh8DBQxBbGxlcyB3aXNzZW5kZALDAQ8PFgIeCEltYWdlVXJsBRVJbWFnZXMvcHJveHlfUV9OTC5naWZkZAIKDxYCHwJoFgQCAw8WAh8CaGQCBQ8WAh8CaGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgkFFWN0bEJOJGNoa1ZsYWFtc0dld2VzdAUVY3RsQk4kY2hrTWluZGVydmFsaWRlBRxjdGxCTiRjaGtNaW5kZXJ2YWxpZGVQYXJ0bmVyBQ9jdGxCTiRjaGtKb25nZXIFEmN0bEJOJGNoa1ZEU29jQWJvbgUQY3RsQk4kY2hrVkRGaWV0cwURY3RsQk4kY2hrVkRHcm9lcHMFFWN0bEJOJGNoa1ZERmlybWF3YWdlbgUNY3RsQk4kY2hrVkRNQxRhN9%2B2%2F%2BawAe9M%2Fxrl%2BdTpQqzO&__EVENTVALIDATION=%2FwEWLgLejLrxCgLSlf%2FoAgLh7IThDgLa6PnoAQK7l7CfDgKF%2Bui0AwLQj46VAgKhibCQBwK90vCBBwKCsfHMCgKLhN%2FzCwKZ%2BqACApfJ3ZIGAuCVm8wGAtvBiPoCAva0wa4HAuPdovYCApbc9o8PAryGjoUKAquVqfMKApXsicUFApr7mHYC%2Bpyr1A8C4o2KwwoC842KwwoC24GV6wgC07Pb4QYCvJ%2BpjgoC7Nyxkg0Ct5iIogwCgNfbBgL6%2F6y6CQKk5e3WBgK1i9%2B8BQLmqaL%2FAQKvwfiZDgL%2F2r7gDQKf07cUAoDXtxQCiP7p%2FAsCtbzhkA4C867R8gQCr7jQ3g0CyvXP0Q4Cmqjr5g4C44n5ggMcnQM0BEtR2P6ssJ%2FBkbWqemv%2BfQ%3D%3D&ctlBN%24txtNaam=&ctlBN%24txtVoornaam=&ctlBN%24pmcBurgStaat=01&ctlBN%24chkVlaamsGewest=on&ctlBN%24pmcBeroepPartner=99&ctlBN%24txtTLKindVal=0&ctlBN%24txtTLKindMinVal=0&ctlBN%24txtTLJongVal=0&ctlBN%24txtTLJongMinVal=0&ctlBN%24txtTLOudVal=0&ctlBN%24txtTLOudMinVal=0&ctlBN%24rbStatuut=CLERK&ctlBN%24pmcTewerkstelling=0&ctlBN%24txtUrenPerWeek=38&ctlBN%24txtWerkdagenPerWeek=&ctlBN%24txtBrutoMaandloon=""" + str(loon) + """&ctlBN%24txtBrutoUurloon=&ctlBN%24txtNettoMaandloon=&ctlBN%24txtNettoUurloon=&ctlBN%24cbxSASoort=OV&ctlBN%24txtSABedrag=&ctlBN%24txtFietsAantalKm=&ctlBN%24txtFietsBedrag=&ctlBN%24txtGroepsWnBijdr=&ctlBN%24txtFWWnBijdr=&ctlBN%24txtCO2Uitstoot=&ctlBN%24txtCatalogusWaarde=&ctlBN%24txtDatumInschrijving=&ctlBN%24pmcTypeBrandstof=1&ctlBN%24txtMCWgBijdr=&ctlBN%24txtMCWnBijdr=&ctlBN%24txtKosten=&ctlBN%24txtCommissieLoon=&ctlBN%24txtPremies=&ctlBN%24txtAndere=&ctlBN%24btnBrutoNetto=Bruto+%3D%3E+netto' --compressed"""
    
    import subprocess
    handle = open("tst.txt", "w")
    subprocess.run(h, shell=True, stdout=handle)
    handle.close()
    
    handle = open("tst.txt", "r", encoding="utf8")
    
    
    import re
    for line in handle.readlines():
        if "ctlBN$txtNettoMaandloon" in line:
            t = re.search("value=", line)
            start = line.find('"', t.span()[1])
            end = line.find('"', t.span()[1]+2)
            result.write(str(loon))
            result.write(",")
            result.write(str(float(line[start+1:end].replace(',','.'))))
            result.write("\n")
            result.flush()
            break
    handle.close()




result.close()
