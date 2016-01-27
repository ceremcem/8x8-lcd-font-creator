x-start = 160
y-start = 80
margin = 20

x-end = x-start
y-end = y-start

widget-xml = (widget-class, x, y, name) -->
    template = """
   <widget class="#{widget-class}" name="#{name}">
    <property name="geometry">
     <rect>
      <x>#{x}</x>
      <y>#{y}</y>
      <width>16</width>
      <height>16</height>
     </rect>
    </property>
   </widget>
    """


kled-xml = widget-xml \KLed
checkbox-xml = widget-xml \QCheckBox



for i in [1 to 8]
    for j in [1 to 8]
        x-offset = margin * i
        y-offset = margin * j
        x-pos = x-end + x-offset
        y-pos = y-end + y-offset
        name = "pixel_#{i}_#{j}"
        console.log checkbox-xml x-pos, y-pos, name

x-end = x-pos
y-end = y-pos

for i in [1 to 8]
    for j in [1 to 8]
        x-offset = margin * i
        y-offset = margin * j
        x-pos = x-end + x-offset
        y-pos = y-end + y-offset
        name = "led_#{i}_#{j}"
        console.log kled-xml x-pos, y-pos, name

x-end = x-pos
y-end = y-pos





