function resizeIframe(frameId) {
    var iframe = document.getElementById(frameId);
    if (iframe) {
        iframe.onload = function() {
            var iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            iframe.style.height = iframeDocument.body.scrollHeight + 'px';
        };
    } else {
        console.error('Iframe with ID ' + frameId + ' not found.');
    }
}

window.addEventListener('load', function() {
    resizeIframe('mkdocs-apps');
    resizeIframe('mkdocs-support');
});
