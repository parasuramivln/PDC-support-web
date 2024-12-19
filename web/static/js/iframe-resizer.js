let loaded = false;

// Should make iframe goto underlying pages http://<Main URL>/support/?section=/<Folder>/support-docs/basics/quickstart
// as in https://pdc-web.eecs.kth.se/docs/support/?section=/doc/support-docs/basics/quickstart
// or as https://pdc-web.eecs.kth.se/docs/support/?sub=basics/quickstart

function loadPage(iframe) {
    if (!loaded) {
        urlParams = new URLSearchParams(window.location.search);
        section = urlParams.get('section');
        sub =  urlParams.get('sub');
        fragment = window.location.hash;
        if (sub) {
            if (window.location.href.includes('/doc/support'))
                part_url='/doc/support-docs/';
            if (window.location.href.includes('/doc/applications'))
                part_url='/doc/software-docs/';
            iframe.src = part_url + sub;    
            }
        if (section)
            iframe.src = section;
        loaded=true;
        iframe.onload = function () {
            if (fragment) {
                iframe.contentWindow.location.hash = fragment;
                }
            };
        resizeIframe(iframe)
        }
    }

function resizeIframe(iframe) {
    if (iframe) {
        iframe.onload = function() {
            var iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            iframe.style.height = iframeDocument.body.scrollHeight + 'px';
            };
        }
    else {
        console.error('Iframe with ID ' + frameId + ' not found.');
        }
    }

function toggleMenu() {
    const nav = document.querySelector('nav ul');
    nav.classList.toggle('open');
    }
