import pygame
import random
import sys

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Ukuran papan permainan
ROWS = 25
COLS = 25
CELL_SIZE = SCREEN_WIDTH // COLS

# Kode tipe sel
EMPTY = 0
BOMB = 1
NUMBER = 2

# Kelas abstrak untuk Sel
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.state = EMPTY
        self.output = False
        self.flagged = False

    def draw(self, screen):
        # Metode untuk menggambar sel pada layar.
        if not self.output:
            pygame.draw.rect(screen, GRAY, self.rect)
            if self.flagged:
                font = pygame.font.Font(None, 30)
                text = font.render("F", True, RED)
                text_rect = text.get_rect(center=self.rect.center)
                screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, WHITE, self.rect)
            if self.state == BOMB:
                pygame.draw.rect(screen, RED, self.rect)  # Perubahan warna menjadi merah untuk bomb
            elif self.state == NUMBER:
                font = pygame.font.Font(None, 30)
                text = font.render(str(self.bomb_sekitar), True, BLUE)
                text_rect = text.get_rect(center=self.rect.center)
                screen.blit(text, text_rect)

# Kelas turunan untuk Sel Bom
class BOMB(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.state = BOMB

# Kelas turunan untuk Sel dengan Angka
class NumberCell(Cell):
    def __init__(self, row, col, bomb_sekitar):
        super().__init__(row, col)
        self.state = NUMBER
        self.bomb_sekitar = bomb_sekitar

# Kelas utama game Minesweeper
class Minesweeper:
    def __init__(self):
        # Metode untuk menginisialisasi game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Minesweeper Handayani")
        self.clock = pygame.time.Clock()
        self.running = True
        self.permainan_berakhir = False
        self.score = 0
        self.timer = 0
        self.start_time = None

        # Inisialisasi papan permainan
        self.grid = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
        self.posisi_bomb()
        self.menghitung_angka()

    def update_timer(self):
        # Metode untuk mengupdate timer
        if self.start_time is not None:
            current_time = pygame.time.get_ticks()
            self.timer = (current_time - self.start_time) // 1000

    def posisi_bomb(self):
        # Metode untuk menempatkan bom secara acak pada papan permainan
        bomb_count = COLS * ROWS // 6
        for _ in range(bomb_count):
            row = random.randint(0, ROWS - 1)
            col = random.randint(0, COLS - 1)
            while isinstance(self.grid[row][col], BOMB):
                row = random.randint(0, ROWS - 1)
                col = random.randint(0, COLS - 1)
            self.grid[row][col] = BOMB(row, col)

    def menghitung_angka(self):
        # Metode untuk menghitung jumlah bom yang berdekatan dengan setiap sel non-bom
        for row in range(ROWS):
            for col in range(COLS):
                if not isinstance(self.grid[row][col], BOMB):
                    bomb_sekitar = sum(1 for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                                         if 0 <= row + dr < ROWS and 0 <= col + dc < COLS
                                         and isinstance(self.grid[row + dr][col + dc], BOMB))
                    if bomb_sekitar > 0:
                        self.grid[row][col] = NumberCell(row, col, bomb_sekitar)

    def reveal_cell(self, row, col):
        # Metode untuk mengungkap sel tertentu
        cell = self.grid[row][col]
        if not cell.output and not cell.flagged:
            cell.output = True
            if cell.state == EMPTY:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if 0 <= row + dr < ROWS and 0 <= col + dc < COLS:
                            self.reveal_cell(row + dr, col + dc)
            elif cell.state == NUMBER:
                self.score += 1  # Tambahkan nilai skor ketika sel angka diungkapkan


    def toggle_flag(self, row, col):
        # Metode untuk menandai atau menghapus tanda pada sel tertentu.
        cell = self.grid[row][col]
        if not cell.output:
            cell.flagged = not cell.flagged

    def kemenangan(self):
        # Metode untuk memeriksa apakah semua sel non-bom telah diungkap.
        for row in range(ROWS):
            for col in range(COLS):
                if not isinstance(self.grid[row][col], BOMB) and not self.grid[row][col].output:
                    return False
        return True

    def Kendali(self):
        # Metode untuk menangani event klik mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.permainan_berakhir:
                x, y = event.pos
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                if event.button == 1:
                    if isinstance(self.grid[row][col], BOMB):
                        self.permainan_berakhir = True
                        self.start_time = None
                    else:
                        if self.start_time is None:
                            self.start_time = pygame.time.get_ticks()
                        self.reveal_cell(row, col)
                elif event.button == 3:
                    self.toggle_flag(row, col)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and self.permainan_berakhir:
                self.__init__()
                
    def draw(self):
        # Metode untuk menggambar papan permainan.
        self.screen.fill(BLACK)
        for row in self.grid:
            for cell in row:
                cell.draw(self.screen)
                if self.permainan_berakhir and isinstance(cell, BOMB) and cell.state == BOMB:
                    pygame.draw.rect(self.screen, RED, cell.rect)  # Gambar sel bom dengan warna merah
        if self.permainan_berakhir:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Game Berakhir! Waktu: {self.timer} detik, Skor: {self.score}", True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
        else:
            font = pygame.font.Font(None, 30)
            timer_text = font.render(f"Time: {self.timer} seconds", True, BLACK)
            score_text = font.render(f"Score: {self.score}", True, BLACK)
            self.screen.blit(timer_text, (10, 10))
            self.screen.blit(score_text, (10, 40))
        pygame.display.flip()



    def run(self):
        # Metode utama untuk menjalankan game.
        while self.running:
            self.update_timer()  # Update timer setiap frame
            self.Kendali()
            self.draw()
            self.clock.tick(30)

# Fungsi utama
def main():
    game = Minesweeper()
    game.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
