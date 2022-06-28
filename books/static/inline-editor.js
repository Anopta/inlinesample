function inlineEditor(inlineSetName) {
    let tmpl = document.querySelector('#empty-form-' + inlineSetName);
    let counter = document.querySelector('[name=' + inlineSetName + '-TOTAL_FORMS]')

    document.querySelector('#add-form-' + inlineSetName).addEventListener('click', ev => {
        ev.preventDefault()

        let newForm = tmpl.content.cloneNode(true);
        newForm.querySelectorAll('[id*=__prefix__]').forEach(el => {
            el.id = el.id.replace('__prefix__', counter.value);
            if (el.name) el.name = el.name.replace('__prefix__', counter.value);
        });

        newForm.querySelectorAll('[for*=__prefix__]').forEach(el => {
            el.htmlFor = el.htmlFor.replace('__prefix__', counter.value);
        })

        counter.value = 1 + Number(counter.value);
        let last_element_selector = 'form #better_inline_' + inlineSetName + ' .inline-form:last-of-type'
        document.querySelector(last_element_selector).insertAdjacentElement('afterend', newForm.children[0])
    })
}

function delClick(el) {
    if(el.checked) {
        el.parentElement.parentElement.parentElement.classList.add('border-red-500')
    } else {
        el.parentElement.parentElement.parentElement.classList.remove('border-red-500')
    }
}

document.addEventListener('DOMContentLoaded', function(event) {
    inlineEditor('edition_set');
    inlineEditor('testimonial_set');
})