![](./images/logo.png)
![](./images/img1.png)

NetCat(nc) is a command used for reading or writing data over the network.
It is also called Swiss Army Knife.

### Format of nc
```
nc [domain_name/IP address] [port]
```

On connecting we get a huge lines of strings.So we can redirect the output to a file using
\> operator.

Then we can run grep over it to get the flag.

FLAG:
```
picoCTF{digital_plumb3r_995d3c81}
```
