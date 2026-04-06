document.addEventListener('DOMContentLoaded', () => {
    // Fallback resiliente para assets ausentes:
    // mantém os caminhos originais, mas evita "imagem quebrada" na página.
    const fallbackAsset = './assets/logo-transparente-kportas-svg.svg';
    const pageImages = document.querySelectorAll('img');

    pageImages.forEach((img) => {
        img.addEventListener('error', () => {
            if (img.dataset.fallbackApplied === 'true') return;
            img.dataset.fallbackApplied = 'true';
            img.src = fallbackAsset;
        });
    });
    
    const callbackForm = document.getElementById('callbackForm');
    const callbackPhone = document.getElementById('callbackPhone');

    if (callbackForm && callbackPhone) {
        
        // Máscara Visual para o Telefone (11) 99999-9999
        callbackPhone.addEventListener('input', function (e) {
            let x = e.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,5})(\d{0,4})/);
            e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
        });

        // Ação de Envio: Abrir Aba do WhatsApp com Mensagem Automática
        callbackForm.addEventListener('submit', function (e) {
            e.preventDefault(); // Impede o reload da página
            
            const phoneVal = callbackPhone.value.trim();
            
            if (phoneVal.length >= 14) { // Validação simples de tamanho
                
                // Mensagem requisitada com o número injetado para melhor tracking interno se desejado, 
                // ou apenas a mensagem padrão descrita.
                // Mensagem requisitada pelo usuário para iniciar a conversa via WhatsApp
                const wppMessage = `Olá K Portas, gostaria de uma ligação neste número ${phoneVal} para falar sobre um projeto.`;
                const encodedMessage = encodeURIComponent(wppMessage);
                
                // Abre o WhatsApp na nova aba apontando para o número real (11) 99312-3964
                window.open(`https://wa.me/5511993123964?text=${encodedMessage}`, '_blank');
                
                // UX: Limpa o campo e troca texto do botão temporariamente
                const btn = this.querySelector('button');
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Solicitação Recebida!';
                btn.style.backgroundColor = '#25D366'; // Fica verde
                
                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.backgroundColor = ''; // Volta ao Dourado (#D4AF37) da classe
                    callbackPhone.value = '';
                }, 4000);
            } else {
                alert("Por favor, insira um número de telefone válido com DDD.");
            }
        });
    }

    // --- FAQ Accordion Logic ---
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const currentItem = question.parentElement;
            
            // Fecha todos os outros (Opcional, mas dá elegância)
            document.querySelectorAll('.faq-item').forEach(item => {
                if (item !== currentItem) {
                    item.classList.remove('active');
                }
            });
            
            // Inverte o atual
            currentItem.classList.toggle('active');
        });
    });

});
