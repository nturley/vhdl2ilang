
architecture Behavioral of vga_controller is
constant end_of_frame: integer := vsync_start + v_back_porch - 1;
signal v_counter : unsigned(9 downto 0);
begin
end Behavioral;