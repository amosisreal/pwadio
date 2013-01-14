# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItunesTrackInfo'
        db.create_table('pwadio_be_2_itunestrackinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('wrapper_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('artist_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('collection_Id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('artist_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('collection_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('collection_censored_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_censored_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('collection_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('track_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('preview_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artwork_URL_30', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artwork_URL_60', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artwork_URL_100', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('collection_price', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_price', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('release_date', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('collection_explicitness', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_explicitness', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('disc_count', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('disc_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_count', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_time_millis', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('primary_genre_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content_advisory_rating', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('long_description', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('pwadio_be_2', ['ItunesTrackInfo'])

        # Adding model 'MusicServices'
        db.create_table('pwadio_be_2_musicservices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apiURL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('search_API_URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('search_URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('developer_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be_2', ['MusicServices'])

        # Adding model 'Artist'
        db.create_table('pwadio_be_2_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be_2', ['Artist'])

        # Adding model 'Album'
        db.create_table('pwadio_be_2_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('year_released', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be_2.Artist'])),
        ))
        db.send_create_signal('pwadio_be_2', ['Album'])

        # Adding model 'Track'
        db.create_table('pwadio_be_2_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('year_released', self.gf('django.db.models.fields.DateTimeField')()),
            ('track_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be_2.Artist'])),
        ))
        db.send_create_signal('pwadio_be_2', ['Track'])

        # Adding model 'MusicServices_Artist_Lookup'
        db.create_table('pwadio_be_2_musicservices_artist_lookup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['pwadio_be_2.Artist'])),
            ('music_service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['pwadio_be_2.MusicServices'])),
            ('music_service_object_id_from_web', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be_2', ['MusicServices_Artist_Lookup'])

        # Adding model 'MusicServices_Track_Lookup'
        db.create_table('pwadio_be_2_musicservices_track_lookup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['pwadio_be_2.Track'])),
            ('music_service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['pwadio_be_2.MusicServices'])),
            ('music_service_object_id_from_web', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be_2', ['MusicServices_Track_Lookup'])

        # Adding model 'RadioStation'
        db.create_table('pwadio_be_2_radiostation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('playlist_URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('am_fm_band', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone_1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone_2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=600)),
        ))
        db.send_create_signal('pwadio_be_2', ['RadioStation'])

        # Adding model 'ProcessingTime'
        db.create_table('pwadio_be_2_processingtime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_ID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be_2.RadioStation'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('download_site_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('processing_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('total_elapsed_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('number_of_tracks_added_this_batch', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('pwadio_be_2', ['ProcessingTime'])

        # Adding model 'RunningPlaylist'
        db.create_table('pwadio_be_2_runningplaylist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('processing_time', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be_2.ProcessingTime'])),
            ('Unique_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('time_played', self.gf('django.db.models.fields.DateTimeField')()),
            ('radio_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be_2.RadioStation'])),
            ('artist_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be_2.Artist'])),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be_2.Track'])),
        ))
        db.send_create_signal('pwadio_be_2', ['RunningPlaylist'])


    def backwards(self, orm):
        # Deleting model 'ItunesTrackInfo'
        db.delete_table('pwadio_be_2_itunestrackinfo')

        # Deleting model 'MusicServices'
        db.delete_table('pwadio_be_2_musicservices')

        # Deleting model 'Artist'
        db.delete_table('pwadio_be_2_artist')

        # Deleting model 'Album'
        db.delete_table('pwadio_be_2_album')

        # Deleting model 'Track'
        db.delete_table('pwadio_be_2_track')

        # Deleting model 'MusicServices_Artist_Lookup'
        db.delete_table('pwadio_be_2_musicservices_artist_lookup')

        # Deleting model 'MusicServices_Track_Lookup'
        db.delete_table('pwadio_be_2_musicservices_track_lookup')

        # Deleting model 'RadioStation'
        db.delete_table('pwadio_be_2_radiostation')

        # Deleting model 'ProcessingTime'
        db.delete_table('pwadio_be_2_processingtime')

        # Deleting model 'RunningPlaylist'
        db.delete_table('pwadio_be_2_runningplaylist')


    models = {
        'pwadio_be_2.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year_released': ('django.db.models.fields.DateTimeField', [], {})
        },
        'pwadio_be_2.artist': {
            'Meta': {'object_name': 'Artist'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.itunestrackinfo': {
            'Meta': {'object_name': 'ItunesTrackInfo'},
            'artist_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'artist_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist_view_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'artwork_URL_100': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'artwork_URL_30': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'artwork_URL_60': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'collection_Id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'collection_censored_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'collection_explicitness': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'collection_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'collection_price': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'collection_view_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'content_advisory_rating': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'disc_count': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'disc_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'long_description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'preview_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'primary_genre_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'release_date': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'track_censored_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track_count': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_explicitness': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'track_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_price': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_time_millis': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_view_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'wrapper_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pwadio_be_2.musicservices': {
            'Meta': {'object_name': 'MusicServices'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'apiURL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'developer_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_API_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.musicservices_artist_lookup': {
            'Meta': {'object_name': 'MusicServices_Artist_Lookup'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.MusicServices']"}),
            'music_service_object_id_from_web': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.musicservices_track_lookup': {
            'Meta': {'object_name': 'MusicServices_Track_Lookup'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.MusicServices']"}),
            'music_service_object_id_from_web': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.Track']"})
        },
        'pwadio_be_2.processingtime': {
            'Meta': {'object_name': 'ProcessingTime'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'download_site_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_tracks_added_this_batch': ('django.db.models.fields.IntegerField', [], {}),
            'processing_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'station_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.RadioStation']"}),
            'total_elapsed_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'})
        },
        'pwadio_be_2.radiostation': {
            'Meta': {'object_name': 'RadioStation'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'am_fm_band': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'playlist_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.runningplaylist': {
            'Meta': {'object_name': 'RunningPlaylist'},
            'Unique_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Artist']"}),
            'artist_name_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processing_time': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.ProcessingTime']"}),
            'radio_station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.RadioStation']"}),
            'time_played': ('django.db.models.fields.DateTimeField', [], {}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Track']"}),
            'track_name_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.track': {
            'Meta': {'object_name': 'Track'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'track_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year_released': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['pwadio_be_2']