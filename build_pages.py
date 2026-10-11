import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
MAIN = "https://www.williamgravestechnology.com"


def header(cur):
    def a(href, label, key):
        return '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if cur == key else "", label)
    return '''<header class="top">
  <a class="logo" href="/" aria-label="W-OS Developers home">
    <img class="light" src="/assets/dark_logo.png" alt="William Graves Technology">
    <img class="dark" src="/assets/light_logo.png" alt="">
    <span class="tag">Developers</span>
  </a>
  <nav>%s%s%s<a href="mailto:support@willgraves.co.uk">Contact</a></nav>
</header>''' % (a("/docs.html", "Build", "docs"), a("/submit.html", "Publish", "submit"), a(MAIN + "/products/", "Store", "store"))


FOOTER = '''<footer>
  <div class="fcols">
    <div class="fcol"><h4>Developers</h4><a href="/docs.html">Build an app</a><a href="/submit.html">Publish on W-OS</a><a href="mailto:support@willgraves.co.uk">Developer support</a></div>
    <div class="fcol"><h4>Products</h4><a href="%(m)s/products/w-phone/">W-Phone</a><a href="%(m)s/products/w-desk/">W-Desk</a></div>
    <div class="fcol"><h4>Company</h4><a href="%(m)s/about/">About</a><a href="%(m)s/careers/">Careers</a><a href="%(m)s/press/">Press</a></div>
    <div class="fcol"><h4>Support</h4><a href="%(m)s/support/">Help Center</a><a href="%(m)s/legal/warranties/">Warranty</a><a href="%(m)s/support/contact/">Contact</a></div>
    <div class="fcol"><h4>Legal</h4><a href="%(m)s/legal/">Legal Hub</a><a href="%(m)s/legal/terms/tos.html">Terms of Use</a><a href="%(m)s/legal/privacy/">Privacy Policy</a><a href="%(m)s/legal/cookies/">Cookies</a></div>
    <div class="fcol"><h4>Follow Us</h4><a href="https://www.instagram.com/williamgravestechnology">Instagram</a><a href="https://bsky.app/profile/williamgravestechnology.com">Bluesky</a><a href="https://www.linkedin.com/company/william-graves-technology">LinkedIn</a></div>
  </div>
  <div class="fbottom">
    <picture><source srcset="/assets/light_logo.png" media="(prefers-color-scheme: dark)"><img src="/assets/dark_logo.png" alt="William Graves Technology"></picture>
    <p>&copy; 2026 William Graves Technology. All rights reserved. William Graves Technology is a trademark of William Graves Corporation Ltd, of which it is a subsidiary. All trademarks and registered trademarks are the property of their respective owners.</p>
  </div>
</footer>''' % {"m": MAIN}


def page(name, title, desc, cur, body):
    html = '''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#f8f8f8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141414" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/assets/dark_logo.png">
<link rel="stylesheet" href="/style.css">
</head>
<body>
%s
<main>
%s
</main>
%s
</body>
</html>
''' % (title, desc, header(cur), body, FOOTER)
    open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n").write(html)


page("index.html", "W-OS Developers | William Graves Technology", "Build apps for W-OS and get them into the W-OS App Store.", "home", '''
<section class="hero">
  <span class="eyebrow">W-OS 4 &middot; Windermere</span>
  <h1>Build for <span style="white-space:nowrap">W-OS.</span></h1>
  <p>Every app in the <span style="white-space:nowrap">W-OS</span> App Store is reviewed and approved by our team, and can be updated or withdrawn at any time. Safe for people to install, simple for you to publish.</p>
  <div class="cta"><a class="btn" href="/docs.html">Start building</a><a class="btn ghost" href="/submit.html">How publishing works</a></div>
</section>

<section class="band"><div class="wrap">
  <h2>Three ways to build an app.</h2>
  <p class="sub">Pick whatever fits what you already make.</p>
  <div class="grid">
    <div class="card"><span class="tagpill">BETA</span><h3>Satisfaction</h3><p>W-OS's own language, built to be easier than Swift: no optionals, no generics, plain-English errors. Logic in <code>.satif</code>, screens in <code>.satUI</code>, run from the Developer app.</p></div>
    <div class="card"><h3>Web apps</h3><p>Already have a website? It can ship as an app with its own window and icon. We review the site, then list it in the store.</p></div>
    <div class="card"><h3>Linux apps</h3><p>Flatpak apps from Flathub can be listed once our team has reviewed them. No W-OS-specific port needed.</p></div>
  </div>
</div></section>

<section class="band gold"><div class="wrap">
  <h2>You stay in control of your app. So do we.</h2>
  <p class="sub">A curated store, like Apple's: nothing is listed until it has been approved.</p>
  <div class="grid">
    <div class="card"><h3>Reviewed first</h3><p>Devices only install what is on our signed list, so nothing else can appear in the store.</p></div>
    <div class="card"><h3>Updates you can ship</h3><p>New versions go through the same review and reach everyone without waiting for an OS update.</p></div>
    <div class="card"><h3>Withdrawn safely</h3><p>If a problem is found, an app is pulled from the store and marked as no longer available on devices that have it.</p></div>
  </div>
</div></section>
''')

page("docs.html", "Build for W-OS | W-OS Developers", "Your first W-OS app in Satisfaction.", "docs", '''
<div class="wrap page">
  <span class="eyebrow">Build</span>
  <h1>Your first app.</h1>
  <p class="lead">Satisfaction apps are two small files. This is a complete, working counter.</p>
  <div class="note"><b>Beta.</b> The Developer app and Satisfaction are part of the W-OS beta channel. Turn on <i>Beta updates</i> in Settings &rarr; Updates, then open <i>Beta features</i> &rarr; Developer.</div>
  <ol class="steps">
    <li><div><b>Create a project</b>Open the Developer app and choose a name. It makes <code>app.json</code>, <code>main.satif</code> and <code>main.satUI</code> for you.</div></li>
    <li><div><b>Write the logic</b>Variables, functions and a call to <code>render()</code> to redraw the screen.</div></li>
    <li><div><b>Describe the screen</b>A declarative view tree that is re-evaluated against your program's live state.</div></li>
    <li><div><b>Run, then install</b>Run shows it in a window. Install puts it in your own home folder, never touching the OS itself.</div></li>
  </ol>
<pre><code>// main.satif
var count = 0

func increment() {
  count = count + 1
  render()
}

func decrement() {
  count = count - 1
  render()
}</code></pre>
<pre><code>// main.satUI
View {
  Text("Satisfaction Counter")
  Text("Count: \\(count)")
  HStack {
    Button("-") { decrement() }
    Button("+") { increment() }
  }
  Spacer
}</code></pre>
  <h2 class="sec">The language in one table</h2>
  <table>
    <tr><th>Thing</th><th>How it looks</th></tr>
    <tr><td>Values</td><td>numbers, strings, booleans, <code>nil</code>, lists <code>[1, 2]</code>, maps <code>["a": 1]</code>, functions</td></tr>
    <tr><td>Variables</td><td><code>let</code> (fixed) and <code>var</code> (changeable). No type annotations.</td></tr>
    <tr><td>Control flow</td><td><code>if</code>/<code>else</code>, <code>while</code>, <code>for x in list</code>, <code>break</code>, <code>continue</code>, <code>return</code>, <code>cond ? a : b</code></td></tr>
    <tr><td>Strings</td><td>Interpolation: <code>"Count: \\(count)"</code></td></tr>
    <tr><td>Several files</td><td><code>import "name"</code> pulls in another <code>.satif</code> from the same project</td></tr>
    <tr><td>Errors</td><td>Always <code>Line N: what went wrong</code>, in plain English</td></tr>
  </table>
  <p style="color:var(--muted)">One screen file per app for now (<code>main.satUI</code>); extra logic files are supported.</p>
</div>
''')

page("submit.html", "Publish on W-OS | W-OS Developers", "How apps get into the W-OS App Store.", "submit", '''
<div class="wrap page">
  <span class="eyebrow">Publish</span>
  <h1>How apps get into the store.</h1>
  <p class="lead">Like Apple's App Store, the W-OS App Store is curated. Our team approves every app and every update, and can withdraw an app at any time.</p>
  <ol class="steps">
    <li><div><b>Send us your app</b>Email the details below to <a href="mailto:support@willgraves.co.uk?subject=App%20submission" style="text-decoration:underline">support@willgraves.co.uk</a>. A submission form is coming; email is the process for now.</div></li>
    <li><div><b>We review it</b>We check it works on W-OS, does what its description says, and is safe for people to install.</div></li>
    <li><div><b>We list it</b>Approved apps are added to the W-OS signed store list. Devices only trust that list, so nothing else can appear in the store.</div></li>
    <li><div><b>Updates go the same way</b>Send a new version and we review and publish it. We can also withdraw an app if a problem is found.</div></li>
  </ol>
  <h2 class="sec">What to send</h2>
  <table>
    <tr><th>Detail</th><th>Why we need it</th></tr>
    <tr><td>App name, your name or company, short description</td><td>Shown in the store listing</td></tr>
    <tr><td>Category</td><td>Where it appears (Music, Work, Creative, &hellip;)</td></tr>
    <tr><td>How it ships: <b>Satisfaction project</b>, <b>web app (https:// address)</b> or <b>Flatpak ID</b></td><td>Decides how it installs</td></tr>
    <tr><td>An icon (SVG preferred)</td><td>The store and launcher tile</td></tr>
    <tr><td>Privacy: what data it collects, if any</td><td>We will not list apps that hide this</td></tr>
    <tr><td>Contact for problems</td><td>So we can reach you if an update is needed</td></tr>
  </table>
  <h2 class="sec">What we won't list</h2>
  <ul class="plain">
    <li>Apps that collect data without saying so</li>
    <li>Apps that ask for more access than they need, or try to reach outside their own folders</li>
    <li>Apps that copy another app's name or branding</li>
    <li>Web apps that are not served over <code>https://</code></li>
  </ul>
  <div class="note">Review times, fees and revenue terms have not been set yet. We will publish them here before opening submissions widely.</div>
</div>
''')
print("pages written")
