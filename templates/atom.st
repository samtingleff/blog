<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
 <title>Sam Tingleff</title>
 <subtitle>fresh nonsense, whenever</subtitle>
 <link rel="alternate" type="text/html" href="http://sam.tingleff.com/" />
 <link rel="self" type="application/atom+xml" href="http://sam.tingleff.com/atom.xml" />
 <id>http://sam.tingleff.com/atom.xml</id>
 <updated>$buildDate$</updated>
 <rights>Copyright 2014, Sam Tingleff</rights>
 $items:{item|
  <entry>
   <title>$item.title$</title>
   <link rel="alternate" type="text/html" href="http://sam.tingleff.com/blog/$item.href$"/>
   <id>tag:sam.tingleff.com,2015-01-16:/$item.slug$</id>
   <published>$item.pubDateRSS$</published>
   <updated>$item.pubDateRSS$</updated>
   <author>
    <name>$item.author$</name>
    <uri>http://sam.tingleff.com/</uri>
   </author>
   <content type="html" xml:lang="en"><![CDATA[
    $item.body$
   ]]></content>
  </entry>
 }$
</feed>
