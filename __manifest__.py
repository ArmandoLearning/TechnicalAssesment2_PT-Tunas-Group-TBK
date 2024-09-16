{
    'name': 'Ruangan Management',
    'version': '1.0',
    'summary': 'Modul untuk mengelola ruangan dan pemesanan ruangan.',
    'description': 'Modul ini mengelola data master ruangan dan pemesanan ruangan dengan validasi terkait.',
    'author': 'Nama Anda',
    'website': 'http://example.com',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/master_ruangan_views.xml',
        'views/pemesanan_ruangan_views.xml',
        'data/ir_sequence_data.xml',
    ],
    'installable': True,
    'application': True,
}
