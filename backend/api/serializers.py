from rest_framework import serializers

from .models import Shipments


class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = '__all__'

    def validate(self, data):
        shipment_to = data.get('s_to')
        shipment_from = data.get('s_from')
        shipment_end_ts = data.get('s_end_ts')
        shipment_start_ts = data.get('s_start_ts')

        if shipment_to == shipment_from:
            raise serializers.ValidationError('Shipment source and destination are the same!')

        if shipment_end_ts and shipment_start_ts > shipment_end_ts:
            raise serializers.ValidationError('Shipment start timestamp must be lower than end timestamp')

        return data
