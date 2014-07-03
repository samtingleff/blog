<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <meta http-equiv="content-language" content="en-US"/>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
  $page.author:{author|<meta name="author" content="$author$"/>}$
  $page.description:{description|<meta name="description" content="$description$"/>}$
  $page.keywords:{keywords|<meta name="keywords" content="$keywords$"/>}$
  <link rel="canonical" href="http://sam.tingleff.com/blog/$page.slug$"/>
  <link rel="stylesheet" href="/blog/static/themes/pyrmontv2/css/style.css" type="text/css" media="all"/>
  <link rel="alternate" type="application/rss+xml" title="sam.tingleff.com RSS Feed" href="http://sam.tingleff.com/blog/feed.rss"/>
  <title>$page.title$</title>
 </head>
 <body>

  <div id="page_wrap">

   <div id="header">
    <div class="blog_title">
     <h1><a href="/blog/">sam tingleff</a></h1>
     <p class="description"></p>
    </div>
    <div class="clear"></div>
   </div><!-- /div header -->

   <div id="main_navi">
    <ul class="left">
     <li class="current_page_item"><a href="/blog/">Home</a></li>
    </ul>
    <ul class="right">
     <li>
         <a href="/blog/feed.rss"><img src="/blog/static/icons/16x16/feed-14x14.png" width="14" height="14"/></a>
     </li>
     <li>
         <a href="http://twitter.com/samtingleff"><img src="/blog/static/icons/16x16/twitter-16x16.png" width="16" height="16"/></a>
     </li>
     <li>
         <a href="https://github.com/samtingleff"><img src="/blog/static/icons/16x16/github-16x16.png" width="16" height="16"/></a>
     </li>
     <li>
         <a href="http://www.linkedin.com/in/samtingleff"><img src="/blog/static/icons/16x16/linkedin-16x16.png" width="16" height="16"/></a>
     </li>
     <!--<li>
         <a href="http://www.flickr.com/photos/samtingleff/"><img src="/blog/static/icons/16x16/flickr-16x16.png" width="16" height="16"/></a>
     </li>-->
    </ul>
   </div><!-- /div main_navi -->

   <div class="clear"></div>

   <div id="container">
    <div id="main">

     <div class="post" id="post-8">

      <div class="date">
       $page.pubDateHtmlShort$
      </div><!-- /div date -->

      <div class="title">
       <h2><a href="/~stingleff/blog/output/$page.slug$" rel="bookmark" title="$page.title$">$page.title$</a></h2>
       <div class="postmeta">
        <!--Tags: $page.tags:{tag| $tag$ }$-->
       </div><!-- /div postmeta -->
      </div><!-- /div title -->

      <div class="clear"></div>

      <div class="entry">
       $page.body$
      </div><!-- /div entry -->

     </div><!-- /div post -->

     <div class="navigation">
      <div class="left"></div>
      <div class="right"></div>
      <div class="clear"></div>
     </div><!-- /div navigation -->

    </div><!-- /div main -->

   <div class="clear"></div>

   </div><!-- /div container -->

  </div><!-- /div page_wrap -->

  $footer()$

 </body>
</html>
