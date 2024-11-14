let loaded = false;

// Should make iframe goto underlying pages http://<Main URL>/support/?section=/<Folder>/support-docs/basics/quickstart
// as in https://pdc-web.eecs.kth.se/docs/support/?section=/docs/support-docs/basics/quickstart

function loadPage(iframe) {
    if (!loaded) {
        urlParams = new URLSearchParams(window.location.search);
        section = urlParams.get('section');
        if (section)
            iframe.src = section;
        loaded=true;
        resizeIframe(iframe)
    }
}

function resizeIframe(iframe) {
    if (iframe) {
        iframe.onload = function() {
            var iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            iframe.style.height = iframeDocument.body.scrollHeight + 'px';
        };
    } else {
        console.error('Iframe with ID ' + frameId + ' not found.');
    }
}
