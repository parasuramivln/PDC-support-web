document.addEventListener('DOMContentLoaded', function () {
    if (window == window.top) {
        let currentURL = window.location.pathname;
        if (currentURL.includes('/support-docs')) {
            let newUrl = currentURL.replace('/support-docs/','/support/?sub=');
            window.location.replace(newUrl);
            }
        }

    document.querySelectorAll('a').forEach(function (link) {
        if (link.hostname !== window.location.hostname) {
            link.target = '_blank';
            }
        });
    });
