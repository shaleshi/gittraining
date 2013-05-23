  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>gittraining/linux/stringcomp[].sh at master · Sadashiv/gittraining · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="xhr-socket" href="/_sockets" />


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="aTGdVpjIAzisR0WEkBNBRj0JCr8wmLMiA2FCGTgRv1s=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-159290696eb4150b6abdc4ac7fa8da500bcca10f.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-98ffc71aa2fdddf77bc5c07502bd431663556ad8.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-92d138f450f2960501e28397a2f63b0f100590f0.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-985d93aa3883d59a41ea7cdb294c66693dfd97e4.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="32c44dcef739ab4f632b714012f5c284">

        <link data-pjax-transient rel='permalink' href='/Sadashiv/gittraining/blob/fea1270420fe309ef451807942874799d876baec/linux/stringcomp%5B%5D.sh'>
    <meta property="og:title" content="gittraining"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/Sadashiv/gittraining"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/063e4a9ab133c0792f0b50534e2ced93?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Contribute to gittraining development by creating an account on GitHub."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="Sadashiv/gittraining"/>

    <meta name="description" content="Contribute to gittraining development by creating an account on GitHub." />


    <meta content="1003414" name="octolytics-dimension-user_id" /><meta content="4321228" name="octolytics-dimension-repository_id" />
  <link href="https://github.com/Sadashiv/gittraining/commits/master.atom" rel="alternate" title="Recent Commits to gittraining:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production  ">
    <div id="wrapper">

      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">Github</a>

    <div class="header-actions">
      <a class="button primary" href="https://github.com/signup">Sign up</a>
      <a class="button" href="https://github.com/login?return_to=%2FSadashiv%2Fgittraining%2Fblob%2Fmaster%2Flinux%2Fstringcomp%5B%5D.sh">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">


      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore</a></li>
        <li class="features"><a href="https://github.com/features">Features</a></li>
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="octicon octicon-gear "></span></a>

  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
      data-repo="Sadashiv/gittraining"
      data-branch="master"
      data-sha="0aac9db5ba329a785b56780ff1a235f497664420"
  >

    <input type="hidden" name="nwo" value="Sadashiv/gittraining" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

  <div class="divider-vertical"></div>

</form>
    </div>

  </div>
</div>


      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2FSadashiv%2Fgittraining"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="octicon octicon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/Sadashiv/gittraining/stargazers">
        1
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2FSadashiv%2Fgittraining"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/Sadashiv/gittraining/network" class="social-count">
        0
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo"></span>
                <span class="author vcard">
                  <a href="/Sadashiv" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">Sadashiv</span>
                  </a></span> /
                <strong><a href="/Sadashiv/gittraining" class="js-current-repository">gittraining</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/Sadashiv/gittraining/pulse" class="js-selected-navigation-item " data-selected-links="pulse /Sadashiv/gittraining/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/Sadashiv/gittraining" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /Sadashiv/gittraining">Code</a></li>
    <li><a href="/Sadashiv/gittraining/network" class="js-selected-navigation-item " data-selected-links="repo_network /Sadashiv/gittraining/network">Network</a></li>
    <li><a href="/Sadashiv/gittraining/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /Sadashiv/gittraining/pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/Sadashiv/gittraining/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /Sadashiv/gittraining/issues">Issues <span class='counter'>0</span></a></li>



    <li><a href="/Sadashiv/gittraining/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /Sadashiv/gittraining/graphs">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/Sadashiv/gittraining/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /Sadashiv/gittraining/tags">Tags <span class="counter ">1</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="octicon octicon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/Sadashiv/gittraining/blob/buildout/linux/stringcomp%5B%5D.sh" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="buildout" rel="nofollow" title="buildout">buildout</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/Sadashiv/gittraining/blob/django/linux/stringcomp%5B%5D.sh" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="django" rel="nofollow" title="django">django</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/Sadashiv/gittraining/blob/gitolite/linux/stringcomp%5B%5D.sh" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="gitolite" rel="nofollow" title="gitolite">gitolite</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/Sadashiv/gittraining/blob/jenkins/linux/stringcomp%5B%5D.sh" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="jenkins" rel="nofollow" title="jenkins">jenkins</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/Sadashiv/gittraining/blob/master/linux/stringcomp%5B%5D.sh" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/Sadashiv/gittraining/blob/zope_app/linux/stringcomp%5B%5D.sh" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="zope_app" rel="nofollow" title="zope_app">zope_app</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/Sadashiv/gittraining/blob/v1.1/linux/stringcomp%5B%5D.sh" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="v1.1" rel="nofollow" title="v1.1">v1.1</a>
                </div> <!-- /.select-menu-item -->
            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/Sadashiv/gittraining" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /Sadashiv/gittraining">Files</a></li>
    <li><a href="/Sadashiv/gittraining/commits/master" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /Sadashiv/gittraining/commits/master">Commits</a></li>
    <li><a href="/Sadashiv/gittraining/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /Sadashiv/gittraining/branches" rel="nofollow">Branches <span class="counter ">6</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:496d930e59716463bb97819fb1a85527 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:496d930e59716463bb97819fb1a85527 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Sadashiv/gittraining" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">gittraining</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Sadashiv/gittraining/tree/master/linux" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">linux</span></a></span><span class="separator"> / </span><strong class="final-path">stringcomp[].sh</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="linux/stringcomp[].sh" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>

      <a href="/Sadashiv/gittraining/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/Sadashiv/gittraining/contributors/master/linux/stringcomp%5B%5D.sh">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif?1359500886" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/Sadashiv/gittraining/blob/fea1270420fe309ef451807942874799d876baec/linux/stringcomp%5B%5D.sh" data-title="gittraining/linux/stringcomp[].sh at master · Sadashiv/gittraining · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">executable file</span>
                  <span>19 lines (18 sloc)</span>
                <span>0.515 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/Sadashiv/gittraining/raw/master/linux/stringcomp%5B%5D.sh" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/Sadashiv/gittraining/blame/master/linux/stringcomp%5B%5D.sh" class="button minibutton ">Blame</a>
                  <a href="/Sadashiv/gittraining/commits/master/linux/stringcomp%5B%5D.sh" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-shell js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/bin/sh</span></div><div class='line' id='LC2'><span class="c">#[] by uisng these operators we can compare the string</span></div><div class='line' id='LC3'><span class="k">if</span> <span class="o">[</span> <span class="nv">$# </span>-eq 0 <span class="o">]</span> ; <span class="k">then</span></div><div class='line' id='LC4'><span class="k">    </span><span class="nb">echo</span> <span class="s2">&quot;Enter the string to be searched:\c&quot;</span></div><div class='line' id='LC5'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">read </span>pname</div><div class='line' id='LC6'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="o">[</span> -z <span class="s2">&quot;$pname&quot;</span><span class="o">]</span> ; <span class="k">then</span>  <span class="c"># -z checks for null string</span></div><div class='line' id='LC7'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">echo</span> <span class="s2">&quot;You have entere not the string&quot;</span> ; <span class="nb">exit </span>1</div><div class='line' id='LC8'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">fi</span></div><div class='line' id='LC9'><span class="k">    </span><span class="nb">echo</span> <span class="s2">&quot;Enter the  file name to be used:\c&quot;</span></div><div class='line' id='LC10'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">read </span>fname</div><div class='line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="o">[</span> ! -n <span class="s2">&quot;$fname&quot;</span> <span class="o">]</span> ; <span class="k">then</span> <span class="c">#-n is same as -z</span></div><div class='line' id='LC12'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">echo</span> <span class="s2">&quot;you have not entered the file name&quot;</span> ; <span class="nb">exit </span>2</div><div class='line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">fi</span></div><div class='line' id='LC14'><span class="k">    </span>test.sh <span class="s2">&quot;$pname&quot;</span> <span class="s2">&quot;$fname&quot;</span> </div><div class='line' id='LC15'><span class="k">else</span></div><div class='line' id='LC16'><span class="k">    </span>test.sh <span class="nv">$*</span></div><div class='line' id='LC17'><span class="c">#    test.sh $@</span></div><div class='line' id='LC18'><span class="k">fi</span> </div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1359500886" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="https://github.com/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.08180s from fe19.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/Sadashiv/gittraining/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="octicon octicon-remove-close ajax-error-dismiss"></a>
    </div>

    
    <span id='server_response_time' data-time='0.08225' data-host='fe19'></span>
    
  </body>
</html>

