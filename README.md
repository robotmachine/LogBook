# LogBook
### Project focused journal utility

#### Install
1. Download [the archive](https://github.com/robotmachine/LogBook/tarball/master)
1. Run `chmod +x lb`
3. Move `lb` to `/usr/local/bin/` or somewhere else in `$PATH`

#### Usage
Pick a location for your journals and add that to a `.lbrc` file:  
```
$> cat .lbrc
[journal]
journaldir = ~/Journal
```

When `lb` is run it will ask about the project you are working on and give some space for general thoughts afterward.  
Files are stored in your Journal directory by year and month.   
