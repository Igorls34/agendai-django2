window.Availability = (function () {
    let endpoint = null;
    let serviceId = null;

    function onDateChange(ev) {
        const dateInput = ev.target;
        const dateValue = dateInput.value;
        if (!dateValue) return;
        fetch(`${endpoint}?service=${serviceId}&date=${dateValue}`)
            .then(r => r.json())
            .then(data => {
                const wrap = document.getElementById('slot-container');
                if (!wrap) return;
                // Limpa e injeta botões de horários
                wrap.innerHTML = '';
                if (!data.slots || data.slots.length === 0) {
                    const p = document.createElement('p');
                    p.className = 'text-sm text-slate-500';
                    p.textContent = 'Sem horários disponíveis nesta data.';
                    wrap.appendChild(p);
                    const fallback = document.getElementById('id_time');
                    if (fallback) fallback.value = '';
                    return;
                }
                data.slots.forEach(t => {
                    const btn = document.createElement('button');
                    btn.type = 'button';
                    btn.className = 'btn';
                    btn.textContent = t;
                    btn.addEventListener('click', () => {
                        const input = document.getElementById('id_time');
                        if (input) input.value = t;
                    });
                    wrap.appendChild(btn);
                });
                // Garante que exista o input time (caso template seja alterado)
                if (!document.getElementById('id_time')) {
                    const hidden = document.createElement('input');
                    hidden.type = 'time';
                    hidden.name = 'time';
                    hidden.id = 'id_time';
                    hidden.required = true;
                    hidden.className = 'input';
                    wrap.appendChild(hidden);
                }
            })
            .catch(() => { /* silencioso */ });
    }

    function init(opts) {
        endpoint = opts.endpoint;
        serviceId = opts.serviceId;
        const dateInput = document.getElementById('id_date');
        if (dateInput) {
            dateInput.addEventListener('change', onDateChange);
        }
    }

    return { init };
})();
