// static/js/main.js
console.log("🚀 ShowTrials Web App - Versão com Lazy Loading");

// Funções utilitárias
function formatDate(dateString) {
    if (!dateString) return "N/D";
    return dateString.substring(0, 10);
}

function truncate(text, length = 50) {
    if (!text) return "";
    return text.length > length ? text.substring(0, length) + "…" : text;
}

// Inicialização
document.addEventListener('DOMContentLoaded', function () {
    console.log("📋 DOM carregado");

    // Ativar tooltips do Bootstrap se disponíveis
    if (typeof bootstrap !== 'undefined') {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});

// Feedback para ações assíncronas
window.showToast = function (message, type = 'info') {
    // Implementar toast notifications
    alert(message); // Placeholder
};