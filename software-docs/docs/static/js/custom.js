document.addEventListener('DOMContentLoaded', function () {
    if (window == window.top) {
        let currentURL = window.location.pathname;
        if (currentURL.includes('/software-docs')) {
            let newUrl = currentURL.replace('/software-docs/','/applications/?sub=');
            window.location.replace(newUrl);
            }
        }

    document.querySelectorAll('a').forEach(function (link) {
        if (link.hostname !== window.location.hostname) {
            link.target = '_blank';
        }
    });
});
