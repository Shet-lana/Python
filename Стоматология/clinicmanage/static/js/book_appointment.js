document.addEventListener('DOMContentLoaded', function () {
    const doctorSelect = document.getElementById('id_dentist');
    const dateInput = document.getElementById('appointment_date');
    const timeSelect = document.getElementById('appointment_time');
    const loading = document.getElementById('loading');
    const noSlots = document.getElementById('no-slots');
    const form = document.getElementById('appointment-form');

    // Создаём скрытое поле для полной даты и времени
    let hiddenDateTime = document.getElementById('appointment_datetime');
    if (!hiddenDateTime) {
        hiddenDateTime = document.createElement('input');
        hiddenDateTime.type = 'hidden';
        hiddenDateTime.name = 'appointment_datetime';
        hiddenDateTime.id = 'appointment_datetime';
        form.appendChild(hiddenDateTime);
    }

    function loadAvailableSlots() {
        // Получаем doctor_id: из select или из скрытого поля (например, при переносе визита)
        const doctorId = doctorSelect
            ? doctorSelect.value
            : document.getElementById('doctor_id')?.value;

        const selectedDate = dateInput.value;

        if (!doctorId || !selectedDate) {
            if (timeSelect) {
                timeSelect.innerHTML = '<option value="">--- Выберите дату ---</option>';
            }
            return;
        }

        if (timeSelect) {
            timeSelect.innerHTML = '<option value="">--- Загрузка ---</option>';
        }
        if (noSlots) noSlots.style.display = 'none';
        if (loading) loading.style.display = 'block';

        // Формируем URL
        const url = `/get-available-slots-json/?date=${selectedDate}&doctor_id=${doctorId}`;
        console.log('Fetching:', url);

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (loading) loading.style.display = 'none';
                console.log('Slots received:', data);

                // Получаем текущее время
                const now = new Date();
                const today = now.toISOString().split('T')[0]; // YYYY-MM-DD
                const currentHour = now.getHours(); // 0–23

                let availableSlots = data.slots || [];

                // Если выбрана текущая дата — исключаем прошедшие часы
                if (selectedDate === today) {
                    availableSlots = availableSlots.filter(slot => {
                        const slotHour = parseInt(slot.split(':')[0]); // Час из "08:00"
                        return slotHour > currentHour; // Только будущие часы
                    });
                }

                // Обновляем select
                if (timeSelect) {
                    if (availableSlots.length === 0) {
                        timeSelect.innerHTML = '<option value="">Нет доступного времени</option>';
                        if (noSlots) noSlots.style.display = 'block';
                    } else {
                        let options = '<option value="">--- Выберите время ---</option>';
                        availableSlots.forEach(slot => {
                            options += `<option value="${slot}">${slot}</option>`;
                        });
                        timeSelect.innerHTML = options;
                    }
                }
            })
            .catch(err => {
                if (loading) loading.style.display = 'none';
                console.error('Ошибка при загрузке слотов:', err);
                if (timeSelect) {
                    timeSelect.innerHTML = '<option value="">Ошибка загрузки</option>';
                }
            });
    }

    // Обновляем скрытое поле при выборе времени
    if (timeSelect) {
        timeSelect.addEventListener('change', function () {
            const selectedDate = dateInput.value;
            const selectedTime = this.value;

            if (selectedDate && selectedTime) {
                hiddenDateTime.value = `${selectedDate}T${selectedTime}`;
            } else {
                hiddenDateTime.value = '';
            }
        });
    }

    // Подписываемся на изменения даты и врача
    if (dateInput) {
        dateInput.addEventListener('change', loadAvailableSlots);
    }

    if (doctorSelect) {
        doctorSelect.addEventListener('change', loadAvailableSlots);
    } else {
        // Если нет выбора врача — вызываем при изменении даты
        dateInput.addEventListener('change', loadAvailableSlots);
    }
});