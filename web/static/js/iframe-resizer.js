let loaded = false;

// Should make iframe goto underlying pages http://<Main URL>/support/?section=/<Folder>/support-docs/basics/quickstart
// or as https://pdc-web.eecs.kth.se/docs/support/?sub=basics/quickstart
function loadPage(iframe) {
    if (!loaded) {
        urlParams = new URLSearchParams(window.location.search);
        sub =  urlParams.get('sub');
        if (sub) {
            if (window.location.pathname.includes('/support/'))
                part_url = window.location.pathname.replace('/support/','/support-docs/');
            if (window.location.pathname.includes('/applications/'))
                part_url=window.location.pathname.replace('/applications/','/software-docs/');
            iframe.src = part_url + sub;    
            }
        loaded=true;
        resizeIframe(iframe)
        }
    }

function resizeIframe(iframe) {
    if (iframe) {
        iframe.onload = function() {
            var iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            iframe.style.height = iframeDocument.body.scrollHeight + 'px';
            fragment = window.location.hash;
            targetElement = iframe.contentDocument.querySelector(fragment);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
                }
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
