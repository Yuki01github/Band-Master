from configparser import ConfigParser
from os.path import dirname, join


def config_writing(self):
    config = ConfigParser()
    section1 = 'path'
    config.add_section(section1)
    config.set(section1, 'src', self.entry_input.get())
    config.set(section1, 'dst', self.entry_output.get())

    section2 = 'values'
    config.add_section(section2)
    config.set(section2, 'title', self.entry_title.get())
    config.set(section2, 'xlabel', self.entry_xaxis.get())
    config.set(section2, 'ylabel', self.entry_yaxis.get())
    config.set(section2, 'legend1', self.entry1_1.get())
    config.set(section2, 'legend2', self.entry2_1.get())
    config.set(section2, 'legend3', self.entry3_1.get())
    config.set(section2, 'srf', str(self.bln_src.get()))  # 編集
    config.set(section2, 'gridf', str(self.bln_gridflag.get()))
    config.set(section2, 'flag_line', str(self.bln_line.get()))
    config.set(section2, 'flag_leaky', str(self.bln_lightcone.get()))
    config.set(section2, 'legendf', str(self.bln_legendflag.get()))
    config.set(section2, 'normf', str(self.bln_norm.get()))
    config.set(section2, 'gtype', str(self.gtype.get()))  # 編集
    config.set(section2, 'gsize', str(self.gsize.get()))  # 編集
    config.set(section2, 'xmin', self.entry_xrange1.get())
    config.set(section2, 'xmax', self.entry_xrange2.get())
    config.set(section2, 'ymin', self.entry_yrange1.get())
    config.set(section2, 'ymax', self.entry_yrange2.get())
    config.set(section2, 'lat_const', self.entry_lat_const.get())

    with open(f'{dirname(__file__)}\\config.ini', 'w') as f:
        config.write(f)


def config_reading():
    path = join(dirname(__file__), "config.ini")
    config = ConfigParser()
    config.read(path)
    return config


def gm_config():
    config = ConfigParser()
    config['DEFAULT'] = {
        'editor_executable': r''
    }
    with open(f'{dirname(__file__)}\\config.ini', 'w') as f:
        config.write(f)


if __name__ == '__main__':
    config_reading()
