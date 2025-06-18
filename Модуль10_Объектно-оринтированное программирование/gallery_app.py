import flet as ft
from PIL import ImageFilter
from PIL.Image import open as pil_open
import os
import shutil

filter_map = {
    ft.icons.BLUR_ON: ('blur_', ImageFilter.GaussianBlur(20)),
    ft.icons.THEATERS: ('emboss_', ImageFilter.EMBOSS),
    ft.icons.MAN: ('contour_', ImageFilter.CONTOUR),
}

IMAGES = ['image1.png', 'image2.png', 'image3.png']


class GalleryApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window_width = 600
        self.page.window_height = 600
        # self.page.window_resizable = False
        # self.page.window_full_screen = True
        self.page.title = 'Галерея'
        self.page.vertical_alignment = 'center'

        self.current_image_index = 0
        self.images = IMAGES.copy()

        self.flet_img = ft.Image(
            src=self.images[self.current_image_index],
            width=600,
            height=400,
            fit=ft.ImageFit.CONTAIN,
            border_radius=10,
        )

        self.controls = ft.Row(
            [
                ft.IconButton(ft.icons.ARROW_BACK, on_click=self.prev_image),
                ft.IconButton(ft.icons.ARROW_FORWARD, on_click=self.next_image),
                ft.IconButton(ft.icons.BLUR_ON, on_click=self.apply_filter),
                ft.IconButton(ft.icons.THEATERS, on_click=self.apply_filter),
                ft.IconButton(ft.icons.MAN, on_click=self.apply_filter),
                ft.IconButton(ft.icons.ADD_PHOTO_ALTERNATE, on_click=self.add_image),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.file_picker = ft.FilePicker(on_result=self.handle_file_pick)
        self.page.overlay.append(self.file_picker)

        self.page.add(
            ft.Column(
                [
                    self.flet_img,
                    self.controls,
                ],
                horizontal_alignment='center'
            )
        )

    def prev_image(self, e):
        self.current_image_index = (self.current_image_index - 1) % len(self.images)
        self.flet_img.src = self.images[self.current_image_index]
        self.page.update()

    def next_image(self, e):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.flet_img.src = self.images[self.current_image_index]
        self.page.update()

    def apply_filter(self, e: ft.ControlEvent):
        orig_path = self.images[self.current_image_index]
        filtered_filename = filter_map[e.control.icon][0] + os.path.basename(orig_path)

        # Проверка наличия ранее отфильтрованного изображения
        if os.path.exists(filtered_filename):
            print(f'Файл {filtered_filename} уже обработан')
            self.flet_img.src = filtered_filename
        else:
            # Открываем оригинальное изображение и применяем фильтр
            pil_img = pil_open(orig_path)
            pil_img = pil_img.filter(filter_map[e.control.icon][1])

            # Сохраняем новое изображение с применением фильтра
            pil_img.save(filtered_filename)
            self.flet_img.src = filtered_filename

        self.page.update()

    def add_image(self, e):
        self.file_picker.pick_files(
            allow_multiple=True,
            allowed_extensions=['jpg', 'jpeg', 'png', 'gif'],
            file_type=ft.FilePickerFileType.IMAGE,
        )

    def handle_file_pick(self, e: ft.FilePickerResultEvent):
        if not e.files:
            return

        for file in e.files:
            new_path = os.path.basename(file.path)
            shutil.copy(file.path, new_path)

            if new_path not in self.images:
                self.images.append(new_path)

        self.current_image_index = len(self.images) - 1
        self.flet_img.src = self.images[self.current_image_index]
        self.page.update()


def main(page: ft.Page):
    GalleryApp(page)


ft.app(main)