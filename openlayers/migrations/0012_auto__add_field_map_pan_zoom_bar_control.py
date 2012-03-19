# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Map.pan_zoom_bar_control'
        db.add_column('openlayers_map', 'pan_zoom_bar_control', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Map.pan_zoom_bar_control'
        db.delete_column('openlayers_map', 'pan_zoom_bar_control')


    models = {
        'openlayers.map': {
            'Meta': {'object_name': 'Map'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer_switcher_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'navigation_control': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pan_zoom_bar_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scale_line_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'openlayers.rasterlayer': {
            'Meta': {'object_name': 'RasterLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'raster_layers'", 'symmetrical': 'False', 'to': "orm['openlayers.Map']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'openlayers.vectorlayer': {
            'Meta': {'object_name': 'VectorLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer_uri': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'maps': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'vector_layers'", 'symmetrical': 'False', 'to': "orm['openlayers.Map']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['openlayers']